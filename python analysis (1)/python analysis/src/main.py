

from pathlib import Path
from utils.logging_utils import setup_logger, get_project_root
from analysis.ingestion import load_sales
from analysis.cleaning import clean_sales
from analysis.eda import create_charts
from analysis.reporting import export_excel

from utils.logging_utils import get_logger


def main():
    project_root = get_project_root()
    reports_dir = project_root / "reports"
    charts_dir = reports_dir / "charts"
    data_dir = project_root / "data"
    logs_dir = project_root / "logs"

    # Ensure dirs exist
    for d in (reports_dir, charts_dir, logs_dir, data_dir):
        d.mkdir(parents=True, exist_ok=True)

    logger = setup_logger("pipeline")
    logger.info(f"cwd={Path.cwd()} | project_root={project_root}")

    # Load / clean
    data_path = data_dir / "sales.csv"
    df = load_sales(data_path)
    df = clean_sales(df)

    # Charts + Excel
    create_charts(df, charts_dir)
    export_excel(df, reports_dir)

    logger.info("All done. Outputs in reports/ and logs/app.log")

if __name__ == "__main__":
    main()











