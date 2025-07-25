import json
from datetime import datetime
from pathlib import Path


def write_interaction_log(data: dict, log_id: str = None):
    log_dir = Path("logs/interaction_logs")
    log_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
    filename = f"{log_id or 'query'}_{timestamp}.json"
    filepath = log_dir / filename

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return filepath
