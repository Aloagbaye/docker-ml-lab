# ---------- base (shared) ----------
FROM python:3.11-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1
RUN useradd -m -u 1000 appuser
WORKDIR /app

# ---------- deps ----------
FROM base AS deps
COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# ---------- runtime ----------
FROM base AS runtime
# copy installed site-packages from deps layer
COPY --from=deps /usr/local /usr/local
COPY app /app/app
EXPOSE 8000
USER appuser
# Healthcheck so orchestrators know we're good
HEALTHCHECK --interval=30s --timeout=3s --retries=3 CMD \
  wget -qO- http://127.0.0.1:8000/health || exit 1
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# ---------- test (optional target) ----------
FROM runtime AS test
USER root
RUN pip install --no-cache-dir pytest==8.3.3
USER appuser
CMD ["pytest", "-q", "app/tests"]