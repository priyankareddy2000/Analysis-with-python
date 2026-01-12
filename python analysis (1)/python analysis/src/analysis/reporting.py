
# src/analysis/reporting.py
import pandas as pd

def export_excel(df, reports_dir):
    reports_dir.mkdir(parents=True, exist_ok=True)
    report_path = reports_dir / "report.xlsx"
    with pd.ExcelWriter(report_path, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="cleaned_data")
        if {"product", "units"}.issubset(df.columns):
            pivot = pd.pivot_table(df, index="product", values="units",
                                   aggfunc=["sum", "mean", "count"])
            pivot.to_excel(writer, sheet_name="pivots")
