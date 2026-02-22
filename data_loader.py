import pandas as pd
from typing import List


def load_ads(csv_path: str) -> List[str]:
    """
    Load raw ad texts from a CSV file with an `ad_text` column.

    Returns a list of strings for downstream model calls.
    """
    df = pd.read_csv(csv_path)
    if "ad_text" not in df.columns:
        raise ValueError("Expected column 'ad_text' in input CSV")
    # Strip whitespace to avoid prompt noise while preserving content.
    return df["ad_text"].astype(str).str.strip().tolist()
