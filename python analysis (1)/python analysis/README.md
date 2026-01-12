
# Data Analysis Project (Python + VS Code)

A detailed, analyst-friendly project showing how **Python** is used in **data analysis**: ingestion, cleaning, exploratory data analysis (EDA), and reporting—fully runnable and automatable in **VS Code**.

## Features
- **Pandas** ingestion & cleaning
- **EDA charts** (time series, breakdowns, distributions)
- **Excel report** with summary pivots
- **VS Code** tasks for one-click run or hourly schedule
- **Config & .env** for flexible paths and titles
- **Unit tests** for cleaning

## Quick Start
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt

cp .env.example .env
# (Optional) edit .env for REPORT_TITLE, DATA_PATH, OUTPUT_DIR

python src/main.py
```

## Run in VS Code
- Terminal → Run Task → **Run Analysis Now**
- Terminal → Run Task → **Run Analysis Hourly**
- Run and Debug → **Debug Data Analysis**

## Project Structure
```
src/
├─ analysis/
│  ├─ ingestion.py      # load CSV → DataFrame + derive revenue
│  ├─ cleaning.py       # drop invalid rows
│  ├─ eda.py            # charts (PNG)
│  └─ reporting.py      # Excel report
├─ utils/
│  └─ logging_utils.py  # console+file logger
└─ main.py              # orchestrator
```

## Outputs
- Charts: `reports/time_series_*.png`, `reports/product_breakdown_*.png`, `reports/units_distribution_*.png`
- Excel report: `reports/report_*.xlsx`
- Logs: `logs/app.log`

## Customize
- Edit `config/config.yaml` to change paths, chart types, currency.
- Use `.env` to override `DATA_PATH`, `OUTPUT_DIR`, `REPORT_TITLE` without changing code.
- Replace `data/sales.csv` with your dataset; ensure headers: `date,region,product,units,price`.

## Testing
```bash
pytest -q
```

## Next steps
- Add more charts (moving averages, anomalies)
- Add alerts (reuse email/Slack helpers from prior project)
- Export PDF reports (use reportlab) if needed

