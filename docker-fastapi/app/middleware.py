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

# app/middleware.py
import logging
import uuid
from typing import Callable

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

# Access logger (your JSON formatter will pick this up)
logger = logging.getLogger("access")


class RequestIDMiddleware(BaseHTTPMiddleware):
    """
    Adds/propagates an X-Request-ID for each request and emits a concise access log.
    - Reads X-Request-ID if the client sends one; otherwise generates a UUID4.
    - Stores it on request.state.request_id for use in routes/handlers.
    - Echoes it back on the response header (x-request-id).
    """

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        request_id = request.headers.get("x-request-id") or str(uuid.uuid4())
        request.state.request_id = request_id

        response: Response = await call_next(request)
        response.headers["x-request-id"] = request_id

        # Minimal structured access log
        logger.info(
            "access",
            extra={
                "request_id": request_id,
                "path": request.url.path,
                "method": request.method,
                "status_code": response.status_code,
            },
        )
        return response


# Explicit export so "from app.middleware import RequestIDMiddleware" works reliably
__all__ = ["RequestIDMiddleware"]

