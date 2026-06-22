"""
Preprocessing utilities for merging ACLED conflict data with FEWS NET IPC
food security data at the county-month level.

IMPORTANT: the mechanical transformations below (aggregation, pivoting,
merging) are provided as working starting points. The substantive decisions
— which county-name fixes are correct, what lag window to use, how to define
your target variable, how to handle remaining missing values — are yours to
make and justify in your report. Don't take the defaults below as final
answers; treat them as hypotheses to test and document.
"""

import pandas as pd

# Starting point only. Run find_unmatched_counties() after loading both
# datasets, inspect the output, and extend this mapping yourself — this is
# a real data-cleaning decision the rubric expects you to document.
COUNTY_NAME_FIXES = {
    # "acled_spelling": "fewsnet_spelling",
}


def standardize_county_names(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Trim whitespace, title-case, and apply manual name corrections to a
    county column.

    Title-casing is applied because ACLED and FEWS NET use inconsistent
    capitalization for the same counties (e.g., "Aweil east" vs.
    "Aweil East") — this is a mechanical normalization, not a judgment
    call, so it's handled here rather than left as a TODO. After this,
    run find_unmatched_counties() again — the remaining handful of true
    mismatches (different spellings, areas one dataset splits differently
    than the other) are the ones worth your own judgment and documentation.
    """
    df = df.copy()
    df[column] = df[column].astype(str).str.strip().str.title()
    df[column] = df[column].replace(COUNTY_NAME_FIXES)
    return df


def find_unmatched_counties(
    acled: pd.DataFrame, ipc: pd.DataFrame, acled_col: str = "admin2", ipc_col: str = "Area"
) -> set:
    """
    Returns county names present in one dataset but not the other, after
    standardization. Use this output to extend COUNTY_NAME_FIXES above —
    inspect each mismatch and decide whether it's a spelling difference
    (fix it), a genuinely absent county (leave it), or something else.
    """
    acled_names = set(acled[acled_col].unique())
    ipc_names = set(ipc[ipc_col].unique())
    return acled_names.symmetric_difference(ipc_names)


def aggregate_acled_to_county_month(acled: pd.DataFrame) -> pd.DataFrame:
    """
    Roll event-level ACLED data up to one row per county per month.

    TODO: consider whether additional engineered features would strengthen
    your model — e.g., a rolling 3-month average of event_count, a binary
    flag for whether civilian-targeting events occurred, or actor-type
    diversity within the county-month. Justify whichever you add.
    """
    df = acled.copy()
    df["year_month"] = df["event_date"].dt.to_period("M")

    agg = (
        df.groupby(["admin2", "year_month"])
        .agg(
            event_count=("event_id_cnty", "count"),
            fatalities_sum=("fatalities", "sum"),
            fatalities_max=("fatalities", "max"),
            battles_count=("event_type", lambda s: (s == "Battles").sum()),
            violence_civilians_count=(
                "event_type",
                lambda s: (s == "Violence against civilians").sum(),
            ),
            protests_count=("event_type", lambda s: (s == "Protests").sum()),
        )
        .reset_index()
        .rename(columns={"admin2": "county"})
    )
    return agg


def pivot_ipc_wide(ipc: pd.DataFrame) -> pd.DataFrame:
    """
    Pivot the long-format IPC file (one row per phase per area per period)
    into one row per county per assessment period, with each phase's
    population percentage as its own column.

    Filters to Validity period == 'current' only — see data/README.md for
    why the projection rows are excluded from ground-truth labels.
    """
    current = ipc[ipc["Validity period"] == "current"].copy()
    current["year_month"] = current["From"].dt.to_period("M")

    wide = current.pivot_table(
        index=["Area", "year_month", "Level 1"],
        columns="Phase",
        values="Percentage",
        aggfunc="first",
    ).reset_index()

    wide.columns.name = None
    wide = wide.rename(
        columns={
            "Area": "county",
            "1": "pct_phase1",
            "2": "pct_phase2",
            "3": "pct_phase3",
            "4": "pct_phase4",
            "5": "pct_phase5",
            "3+": "pct_phase3plus",
        }
    )
    return wide


def merge_conflict_food_security(
    acled_monthly: pd.DataFrame, ipc_wide: pd.DataFrame, lag_months: int = 1
) -> pd.DataFrame:
    """
    Join lagged conflict features to food security outcomes, so conflict
    data always precedes the period it's predicting (avoids leakage).

    TODO: lag_months=1 is a starting default, not a justified choice. Test
    alternative lag windows (e.g., 2 or 3 months) as part of your required
    experiments, and justify your final choice in the report — e.g. with
    reference to FEWS NET's own assessment/reporting cycle, or prior
    literature on the lag between conflict shocks and measurable food
    security impact.
    """
    acled_lagged = acled_monthly.copy()
    acled_lagged["year_month"] = acled_lagged["year_month"] + lag_months

    merged = ipc_wide.merge(acled_lagged, on=["county", "year_month"], how="left")

    conflict_cols = [
        "event_count",
        "fatalities_sum",
        "fatalities_max",
        "battles_count",
        "violence_civilians_count",
        "protests_count",
    ]
    # A missing match means no ACLED-recorded events in that county-month,
    # not a missing observation — fill with 0 rather than dropping.
    merged[conflict_cols] = merged[conflict_cols].fillna(0)

    return merged
