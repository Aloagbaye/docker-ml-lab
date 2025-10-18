import json
import logging
from datetime import datetime

class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        base = {
            "ts": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "logger": record.name,
            "msg": record.getMessage(),
        }
        # include extras like request_id if present
        for key in ("request_id", "path", "method", "status_code"):
            if hasattr(record, key):
                base[key] = getattr(record, key)
        return json.dumps(base)

def configure_logging(level: str = "INFO"):
    handler = logging.StreamHandler()
    handler.setFormatter(JsonFormatter())
    root = logging.getLogger()
    root.handlers.clear()
    root.addHandler(handler)
    root.setLevel(level.upper())
