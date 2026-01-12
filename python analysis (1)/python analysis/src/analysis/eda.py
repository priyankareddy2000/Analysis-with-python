

# src/analysis/eda.py
import matplotlib
matplotlib.use("Agg")  # ensure non-GUI backend for saving PNGs
import matplotlib.pyplot as plt
 

def create_charts(df, charts_dir):
    charts_dir.mkdir(parents=True, exist_ok=True)

    # Time series
    if "date" in df.columns and "units" in df.columns:
        ts = df.groupby("date")["units"].sum().sort_index()
        plt.figure(figsize=(8,4))
        ts.plot(title="Units over time")
        plt.tight_layout()
        (charts_dir / "time_series.png").parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(charts_dir / "time_series.png", dpi=150)
        plt.close()

    # Product breakdown
    if "product" in df.columns and "units" in df.columns:
        prod = df.groupby("product")["units"].sum().sort_values(ascending=False)
        plt.figure(figsize=(6,4))
        prod.plot(kind="bar", title="Units by product")
        plt.tight_layout()
        plt.savefig(charts_dir / "product_breakdown.png", dpi=150)
        plt.close()

    # Units distribution
    if "units" in df.columns:
        plt.figure(figsize=(6,4))
        df["units"].plot(kind="hist", bins=10, title="Units distribution")
        plt.tight_layout()
        plt.savefig(charts_dir / "units_distribution.png", dpi=150)
        plt.close()
