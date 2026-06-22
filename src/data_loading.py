"""
Loaders for the raw ACLED and FEWS NET IPC CSVs used in this project.

Kept deliberately simple (parsing dates, nothing else) — all substantive
cleaning and feature engineering decisions belong in preprocessing.py and
should be made and justified by you, not hidden in a loader function.
"""

import pandas as pd


def load_acled(path: str = "../data/raw/acled_south_sudan.csv") -> pd.DataFrame:
    """Load the raw ACLED conflict event data for South Sudan."""
    return pd.read_csv(path, parse_dates=["event_date"])


def load_ipc(path: str = "../data/raw/fewsnet_ipc_south_sudan.csv") -> pd.DataFrame:
    """Load the raw FEWS NET IPC food security data for South Sudan."""
    return pd.read_csv(path, parse_dates=["From", "To"])
