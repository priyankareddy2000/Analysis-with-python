
import pandas as pd
from src.analysis.cleaning import clean_sales

def test_clean_sales_removes_invalid_rows():
    df = pd.DataFrame({
        "date": ["2026-01-01", None],
        "units": [10, -1],
        "price": [100, 50]
    })
    out = clean_sales(df)
    assert len(out) == 1
