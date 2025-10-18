FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN useradd -m -u 1000 appuser
WORKDIR /app

COPY app/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY app/ /app/

USER appuser

CMD ["python", "predict.py"]
