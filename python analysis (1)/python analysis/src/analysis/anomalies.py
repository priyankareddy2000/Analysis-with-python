
# # src/analysis/anomalies.py
# import pandas as pd

# def flag_revenue_anomalies(df: pd.DataFrame, pct_threshold: float = 0.30) -> pd.DataFrame:
#     """
#     Adds columns:
#       - revenue: already present (units * price)
#       - revenue_pct_change: day-over-day percent change
#       - is_anomaly: 1 if |pct_change| >= pct_threshold else 0
#     Returns a copy with anomaly flags.
#     """
#     out = df.copy()
#     out = out.sort_values("date")
#     out["revenue_pct_change"] = out["revenue"].pct_change()
#     out["is_anomaly"] = (out["revenue_pct_change"].abs() >= pct_threshold).astype(int)
#     return out
