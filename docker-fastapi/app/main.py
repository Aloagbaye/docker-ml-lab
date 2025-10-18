from fastapi import FastAPI
from app.schemas import PredictRequest, PredictResponse
from app.config import settings
from app.logging_conf import configure_logging
from app.middleware import RequestIDMiddleware
import numpy as np
import logging

configure_logging(settings.log_level)
log = logging.getLogger("app")

app = FastAPI(title=settings.app_name, version="1.1")
app.add_middleware(RequestIDMiddleware)

@app.get("/health")
def health():
    return {"status": "ok", "app": settings.app_name}

@app.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest):
    x = np.array(payload.x, dtype=float)
    y = (settings.model_slope * x + settings.model_intercept).tolist()
    log.info("prediction", extra={"request_id": getattr(getattr(payload, "__dict__", {}), "request_id", None)})
    return PredictResponse(input=payload.x, output=y)
