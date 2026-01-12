
# src/analysis/ingestion.py
import pandas as pd

def load_sales(csv_path) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    # Compute revenue if price * units exist
    if {"price", "units"}.issubset(df.columns):
        df["revenue"] = df["price"] * df["units"]
    return df


