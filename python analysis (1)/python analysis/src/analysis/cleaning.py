
# src/analysis/cleaning.py
import pandas as pd

def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    # Example cleaning: drop rows with NA in key columns, non-positive units
    key_cols = [c for c in ("date", "product", "units") if c in df.columns]
    df = df.dropna(subset=key_cols)
    if "units" in df.columns:
        df = df[df["units"] > 0]
    # parse date if present
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df = df.dropna(subset=["date"])
    return df
