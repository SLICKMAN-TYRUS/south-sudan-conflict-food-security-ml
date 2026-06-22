"""
src/data_loading.py
Raw CSV loaders — date parsing only, no cleaning.
All cleaning and feature engineering decisions live in preprocessing.py
so they are visible, documented, and reproducible.
"""

import pandas as pd


def load_acled(path: str = "../data/raw/acled_south_sudan.csv") -> pd.DataFrame:
    """Load raw ACLED conflict event data for South Sudan."""
    return pd.read_csv(path, parse_dates=["event_date"])


def load_ipc(path: str = "../data/raw/fewsnet_ipc_south_sudan.csv") -> pd.DataFrame:
    """Load raw FEWS NET IPC food security phase data for South Sudan."""
    return pd.read_csv(path, parse_dates=["From", "To"])
