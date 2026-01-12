
# src/utils/logging_utils.py
import logging
import sys
from pathlib import Path

def get_project_root() -> Path:
    return Path(__file__).resolve().parents[2]

def get_logger(name: str = "app") -> logging.Logger:
    project_root = get_project_root()
    logs_dir = project_root / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)

    log_file = logs_dir / "app.log"

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

        fh = logging.FileHandler(log_file, encoding="utf-8")
        fh.setFormatter(fmt)

        sh = logging.StreamHandler(sys.stdout)
        sh.setFormatter(fmt)

        logger.addHandler(fh)
        logger.addHandler(sh)

    return logger

# --- Alias so imports of setup_logger work ---
def setup_logger(name: str = "app") -> logging.Logger:
    return get_logger(name)

