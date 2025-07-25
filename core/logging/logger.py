import re
import sys
import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler


class EmojiFilter(logging.Filter):
    def filter(self, record):
        emoji_ranges = [
            '\U0001F600-\U0001F64F', '\U0001F300-\U0001F5FF',
            '\U0001F680-\U0001F6FF', '\U0001F700-\U0001F77F',
            '\U00002500-\U00002BEF', '\U00002702-\U000027B0',
            '\U0001F900-\U0001F9FF',
        ]
        emoji_pattern = re.compile(f"[{''.join(emoji_ranges)}]", flags=re.UNICODE)
        record.msg = emoji_pattern.sub('', str(record.msg))
        return True


LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "app.log"


class LevelBasedFormatter(logging.Formatter):
    def format(self, record):
        if record.levelno == logging.INFO:
            self._style._fmt = "%(asctime)s | %(levelname)-8s | %(filename)s | %(message)s"
        else:
            self._style._fmt = "%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s"
        return super().format(record)


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if logger.hasHandlers():
        return logger

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=2 * 1024 * 1024, backupCount=5)
    file_handler.setLevel(logging.DEBUG)

    formatter = LevelBasedFormatter(datefmt="%Y-%m-%d %H:%M:%S")

    try:
        if hasattr(console_handler.stream, "reconfigure"):
            console_handler.stream.reconfigure(encoding="utf-8")
    except Exception:
        pass

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.addFilter(EmojiFilter())

    return logger
