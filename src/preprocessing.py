"""
src/preprocessing.py
Preprocessing utilities for merging ACLED conflict data with FEWS NET IPC
food security data at the county-month level for South Sudan.

All county-name standardization decisions are documented below and must be
referenced explicitly in the report's methodology section — each fix is a
deliberate, verifiable judgment backed by South Sudan administrative maps,
not an automatic transformation.
"""

import pandas as pd

# ─────────────────────────────────────────────────────────────────────────────
# COUNTY NAME STANDARDIZATION
# Applied to ACLED admin2 to match FEWS NET Area spellings.
# FEWS NET is the label source, so it is the authoritative geographic reference.
#
# THREE FIXES (confirmed against South Sudan administrative maps):
#   "Kajo Keji"  → "Kajo-Keji"  : hyphen formatting difference only
#   "Raja"       → "Raga"        : alternate romanization of the same place
#   "Yei"        → "Yei County"  : FEWS NET appends "County" to disambiguate
#
# SIX DOCUMENTED INTENTIONAL GAPS (do NOT fix — explain each in your report):
#   "Panriang" (ACLED only):
#       A county in Unity State too small/remote for IPC assessment coverage.
#       Events appear in conflict features but have no food security label;
#       these rows are excluded from the merged dataset.
#   "Abyei Region" (FEWS NET only):
#       Disputed territory administered separately from South Sudan; ACLED
#       records its events under Sudan. Food security data retained; conflict
#       features will be zero for this area (not missing).
#   "Akoka" (FEWS NET only):
#       Absent from ACLED admin2, likely subsumed under a broader unit in
#       ACLED's field coding.
#   "East Of Pibor" / "West Of Pibor" (FEWS NET only):
#       FEWS NET split Greater Pibor post-2015 following the creation of the
#       Greater Pibor Administrative Area; ACLED still uses "Pibor". Cannot
#       reliably apportion historical conflict events between East and West.
#   "Wau (Rural Only)" (FEWS NET only):
#       Different scope from ACLED's "Wau" — FEWS NET separately tracks
#       rural areas given Wau city's distinct displacement dynamics.
# ─────────────────────────────────────────────────────────────────────────────
COUNTY_NAME_FIXES = {
    "Kajo Keji": "Kajo-Keji",
    "Raja":      "Raga",
    "Yei":       "Yei County",
}

# Non-geographic FEWS NET population categories to exclude from label data.
# "Returnees" tracks returning displaced persons as a population group,
# not a fixed administrative area — treating it as a county is incorrect.
IPC_NON_GEOGRAPHIC = {"Returnees"}


# ─────────────────────────────────────────────────────────────────────────────
# CLEANING
# ─────────────────────────────────────────────────────────────────────────────

def standardize_county_names(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Trim whitespace, title-case, and apply the three documented name fixes.
    Title-casing resolves most ACLED/FEWS NET capitalisation inconsistencies
    mechanically; COUNTY_NAME_FIXES handles the three substantive differences
    confirmed by cross-referencing South Sudan administrative maps.
    """
    df = df.copy()
    df[column] = df[column].astype(str).str.strip().str.title()
    df[column] = df[column].replace(COUNTY_NAME_FIXES)
    return df


def filter_ipc(ipc: pd.DataFrame) -> pd.DataFrame:
    """
    Retain only IPC current-period assessments and remove non-geographic
    population categories.

    Rationale for excluding projections: FEWS NET's first and second
    projections are analyst forecasts, not observed ground truth. Training on
    projection rows would mean the model learns to imitate FEWS NET's analyst
    judgment rather than predict food security from conflict signals, which
    undermines the project's early-warning framing entirely.
    """
    return ipc[
        (ipc["Validity period"] == "current") &
        (~ipc["Area"].isin(IPC_NON_GEOGRAPHIC))
    ].copy()


def find_unmatched_counties(
    acled: pd.DataFrame,
    ipc:   pd.DataFrame,
    acled_col: str = "admin2",
    ipc_col:   str = "Area",
) -> dict:
    """
    Returns county names present in only one dataset after standardisation.
    After standardize_county_names() and filter_ipc(), the only remaining
    mismatches should be the six documented intentional gaps above.
    Run this in your notebook as a verification step and log its output.
    """
    acled_names = set(acled[acled_col].unique())
    ipc_names   = set(ipc[ipc_col].unique())
    return {
        "only_in_acled": sorted(acled_names - ipc_names),
        "only_in_ipc":   sorted(ipc_names - acled_names),
    }


# ─────────────────────────────────────────────────────────────────────────────
# FEATURE ENGINEERING
# ─────────────────────────────────────────────────────────────────────────────

def aggregate_acled_to_county_month(acled: pd.DataFrame) -> pd.DataFrame:
    """
    Roll event-level ACLED data up to one row per county per calendar month.

    Six conflict features are produced, each linked to a distinct food
    security pathway identified in the literature:
      event_count / fatalities_sum / fatalities_max
          → overall conflict intensity and severity
      battles_count
          → displacement and market/supply-chain disruption
      violence_civilians_count
          → direct food access disruption (looting, movement restriction)
      protests_count
          → political instability and governance breakdown signal

    Extend this function with additional engineered features you justify
    from the literature — for example:
      - rolling_3m_events : smooths monthly spikes, captures chronic conflict
      - civilian_target_flag : binary flag for any civilian-targeting event
      - actor_diversity : number of distinct actors in the county-month
    Each additional feature you add and test is a legitimate experiment
    variation worth logging in your experiment table.
    """
    df = acled.copy()
    df["year_month"] = df["event_date"].dt.to_period("M")

    agg = (
        df.groupby(["admin2", "year_month"])
        .agg(
            event_count              = ("event_id_cnty", "count"),
            fatalities_sum           = ("fatalities",    "sum"),
            fatalities_max           = ("fatalities",    "max"),
            battles_count            = ("event_type",
                                        lambda s: (s == "Battles").sum()),
            violence_civilians_count = ("event_type",
                                        lambda s: (s == "Violence against civilians").sum()),
            protests_count           = ("event_type",
                                        lambda s: (s == "Protests").sum()),
        )
        .reset_index()
        .rename(columns={"admin2": "county"})
    )
    return agg


def pivot_ipc_wide(ipc: pd.DataFrame) -> pd.DataFrame:
    """
    Pivot long-format IPC data (one row per phase per area per period) into
    one row per county per assessment month, with each IPC phase percentage
    as its own column. Assumes filter_ipc() has already been applied.

    Primary prediction target: pct_phase3plus — the percentage of a county's
    population in IPC Phase 3 "Crisis" or worse. This is the standard IPC
    threshold used in humanitarian early-warning literature and operational
    response triggers (IPC Global Partners, 2021).
    """
    df = ipc.copy()
    df["year_month"] = df["From"].dt.to_period("M")

    wide = df.pivot_table(
        index   = ["Area", "year_month", "Level 1"],
        columns = "Phase",
        values  = "Percentage",
        aggfunc = "first",
    ).reset_index()

    wide.columns.name = None
    wide = wide.rename(columns={
        "Area": "county",
        "1":    "pct_phase1",
        "2":    "pct_phase2",
        "3":    "pct_phase3",
        "4":    "pct_phase4",
        "5":    "pct_phase5",
        "3+":   "pct_phase3plus",
        "all":  "pct_all",
    })
    return wide


# ─────────────────────────────────────────────────────────────────────────────
# MERGE
# ─────────────────────────────────────────────────────────────────────────────

def merge_conflict_food_security(
    acled_monthly: pd.DataFrame,
    ipc_wide:      pd.DataFrame,
    lag_months:    int = 1,
) -> pd.DataFrame:
    """
    Left-join lagged conflict features onto food security labels so that
    conflict data always precedes the IPC assessment it predicts. This avoids
    label leakage and reflects a realistic early-warning scenario where only
    historical conflict data would be available at prediction time.

    lag_months=1 is the starting default — test 2 and 3-month lags in your
    required experiments and justify your final choice. The food security
    literature suggests meaningful lag effects operate over 1–3 months after
    acute conflict events (Maystadt & Ecker, 2014; Maxwell et al., 2020).

    Zero-filling logic: a missing conflict match means zero ACLED-recorded
    events in that county-month (no conflict), not a missing observation.
    Filled with 0, not imputed with a non-zero value.
    """
    acled_lagged = acled_monthly.copy()
    acled_lagged["year_month"] = acled_lagged["year_month"] + lag_months

    merged = ipc_wide.merge(acled_lagged, on=["county", "year_month"], how="left")

    conflict_cols = [
        "event_count", "fatalities_sum", "fatalities_max",
        "battles_count", "violence_civilians_count", "protests_count",
    ]
    merged[conflict_cols] = merged[conflict_cols].fillna(0)
    return merged
