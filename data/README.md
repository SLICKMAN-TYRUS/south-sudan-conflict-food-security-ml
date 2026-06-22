# Data Dictionary & Sourcing Notes

## Files expected in `data/raw/`

| Filename | Source | Rows | Description |
|---|---|---|---|
| `acled_south_sudan.csv` | ACLED | 15,725 | Event-level conflict data, 2011–2025 |
| `fewsnet_ipc_south_sudan.csv` | FEWS NET | 25,357 | IPC food security phases, 2017–2026 |

---

## `acled_south_sudan.csv`

**Source:** Armed Conflict Location & Event Data Project (ACLED)
https://acleddata.com — register at acleddata.com/access to download.
**Download filters used:** Country = South Sudan; Date range = 2011-05-19 to
2025-06-21; all event types and actor types included; output = CSV.
**⚠️ Known issue:** Date maximum is 2025-06-21 (one year short of present).
Note this explicitly in your report's methodology section as a data limitation.
**Attribution:** Cite per ACLED Terms of Use: https://acleddata.com/terms-of-use

**Key columns:**

| Column | Type | Description |
|---|---|---|
| `event_date` | date | Date of the conflict event |
| `event_type` | str | Battles / Violence against civilians / Protests / Riots / Explosions / Strategic developments |
| `sub_event_type` | str | Finer-grained event category |
| `actor1` / `actor2` | str | Parties involved |
| `admin1` | str | State (South Sudan's 10 original states) |
| `admin2` | str | County — **join key for merge** |
| `fatalities` | int | Reported fatalities |
| `population_best` | float | People estimated within proximity of the event (~20% missing) |

**Missingness notes:**
- `assoc_actor_1`, `actor2`, `assoc_actor_2`, `civilian_targeting` — structural
  missingness (blank when not applicable). Encode as explicit "N/A" category.
- `population_best` — ~20% genuinely missing. Requires a deliberate handling
  decision (median imputation or drop the feature); justify your choice.
- `admin3`, `tags` — high missingness; not used as features.

---

## `fewsnet_ipc_south_sudan.csv`

**Source:** Famine Early Warning Systems Network (FEWS NET)
https://fews.net — data available at https://fews.net/data
**Coverage:** January 2017 – April 2026, 112 counties.
**Attribution:** Confirm FEWS NET citation policy at fews.net and cite accordingly.

**Key columns:**

| Column | Type | Description |
|---|---|---|
| `Area` | str | County — **join key for merge** |
| `Level 1` | str | State/administrative unit (17 post-2015 units) |
| `Validity period` | str | `current` / `first projection` / `second projection` |
| `From` / `To` | date | Assessment period start and end |
| `Phase` | str | `1`–`5`, `3+` (Crisis-or-worse), `all` |
| `Percentage` | float | Population share in that phase |

**⚠️ Use `current` rows only for labels.** The `first projection` and
`second projection` rows are FEWS NET's own analyst forecasts — training on
them means learning to imitate analysts, not predicting reality from conflict
signals. See `src/preprocessing.py → filter_ipc()` for implementation.

**⚠️ Filter out `Returnees`.** This is a population category, not a county.

---

## County Name Standardization

ACLED `admin2` and FEWS NET `Area` have spelling inconsistencies.
Three fixes are applied in `src/preprocessing.py`:

| ACLED spelling | FEWS NET spelling | Fix applied |
|---|---|---|
| Kajo Keji | Kajo-Keji | Hyphen difference |
| Raja | Raga | Alternate romanization |
| Yei | Yei County | FEWS NET appends "County" |

Six documented **intentional gaps** remain after fixes (explain each in your
methodology section):

| Name | Dataset | Reason not fixed |
|---|---|---|
| Panriang | ACLED only | Too small/remote for IPC assessment |
| Abyei Region | FEWS NET only | Disputed territory; ACLED records under Sudan |
| Akoka | FEWS NET only | Absent from ACLED admin2 coding |
| East Of Pibor | FEWS NET only | Post-2015 split of Greater Pibor; ACLED uses pre-split name |
| West Of Pibor | FEWS NET only | Same as above |
| Wau (Rural Only) | FEWS NET only | Different scope from ACLED's Wau county |

---

## Merge Logic

- **Join level:** county × calendar month (`admin2` / `Area` + `year_month`)
- **Lag:** conflict features shifted forward by 1 month (default) before joining,
  so conflict data always precedes the IPC assessment it predicts.
- **Zero-filling:** a county-month with no ACLED events gets `event_count = 0`,
  not a missing value — it represents zero recorded conflict, not absent data.
- **Overlap period:** January 2017 – June 2025 (1,102 county-month rows after merge)
