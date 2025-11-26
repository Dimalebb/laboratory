import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from config import settings


def setup_logging():
    log_path = Path(settings.log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    root = logging.getLogger()
    root.setLevel(logging.INFO)

    fmt = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    formatter = logging.Formatter(fmt)

    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    root.addHandler(ch)

    fh = RotatingFileHandler(log_path, maxBytes=5_000_000, backupCount=3, encoding="utf-8")
    fh.setFormatter(formatter)
    root.addHandler(fh)

    logging.getLogger("aiogram").setLevel(logging.WARNING)
    logging.getLogger("openai").setLevel(logging.WARNING)