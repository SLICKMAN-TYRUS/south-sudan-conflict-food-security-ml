# Data Dictionary & Sourcing Notes

## `acled_south_sudan.csv`

**Source:** Armed Conflict Location & Event Data Project (ACLED), https://acleddata.com
**Filters used:** Country = South Sudan; Date range = [fill in your corrected
range]; all event types and actor types included.
**Accessed:** [fill in date]
**Attribution:** ACLED data is free to use with attribution — cite per
ACLED's Terms of Use (https://acleddata.com/terms-of-use/) in your report's
reference list (IEEE style).

**Shape:** 15,725 rows × 32 columns (as of this pull).

**Key columns:**
| Column | Description |
|---|---|
| `event_date` | Date of the event |
| `event_type` / `sub_event_type` | Category of political violence/protest (e.g., Battles, Violence against civilians) |
| `actor1` / `actor2` | Parties involved |
| `admin1` | State (10 original states) |
| `admin2` | County |
| `fatalities` | Reported fatalities for the event |
| `population_best` | Estimated population within proximity of the event (conflict exposure measure) |

**⚠️ Known issue:** This pull's `event_date` maximum is 2025-06-21 — one
full year short of the present date. This strongly suggests the export's
"Date To" filter was entered as 2025 instead of 2026. **Re-pull this dataset
with the corrected date range before finalizing your analysis**, especially
since recent conflict trends matter most for an early-warning framing.

**Missingness:** `assoc_actor_1`, `actor2`, `assoc_actor_2`, and
`civilian_targeting` have substantial missing values, but these are
*structural*, not data quality problems — they're blank because they don't
apply to every event (e.g., not every event has a second actor). Encode
these as an explicit "not applicable" category rather than imputing them.
`population_best` is genuinely missing for ~21% of rows and needs a
deliberate, justified handling decision.

---

## `fewsnet_ipc_south_sudan.csv`

**Source:** Famine Early Warning Systems Network (FEWS NET) IPC data,
https://fews.net
**Coverage:** January 2017 – April 2026, 112 counties across all 17
"Level 1" administrative units.
**Accessed:** [fill in date]
**Attribution:** Confirm FEWS NET's current data usage/citation policy at
fews.net before submitting your report, and cite accordingly.

**Shape:** 25,357 rows × 11 columns. No missing values.

**Key columns:**
| Column | Description |
|---|---|
| `Area` | County |
| `Level 1` | State/administrative unit |
| `Validity period` | `current`, `first projection`, or `second projection` — **use `current` only** for ground-truth labels; the projections are FEWS NET's own forecasts and using them as training labels would mean learning to imitate FEWS NET's analysts rather than predicting reality |
| `From` / `To` | Assessment period |
| `Phase` | `1`–`5`, `3+` (crisis-or-worse), or `all` |
| `Percentage` | Share of the area's population in that phase |

**Why this file over the alternative FEWS NET export:** a second, more
granular FEWS NET API export was also available, reaching back to 2011, but
it mixed three different IPC methodology versions (2.0, 3.0, 3.1) across its
timespan, covered fewer counties (81 vs. 112), and only provided a single
ordinal phase value rather than the full percentage breakdown. This file was
chosen for label consistency and analytical richness; the 2011–2016 gap is a
deliberate, documented scoping decision — state this explicitly in your
report's methodology section rather than treating it as a limitation that
"just happened."

---

## Geographic Alignment (for merging the two datasets)

ACLED's `admin1` (10 states) and FEWS NET's `Level 1` (17 units) do **not**
map cleanly to each other — don't join at the state level. Join at the
county level instead (`admin2` vs. `Area`), but expect spelling
inconsistencies between the two sources that need manual review — see
`find_unmatched_counties()` in `src/preprocessing.py`.

A county missing from a given month in the ACLED data means **zero recorded
conflict events there that month**, not missing data — it must be filled
with 0 during aggregation, not dropped.
