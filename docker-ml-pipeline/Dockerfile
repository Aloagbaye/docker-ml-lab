# base slim python image
FROM python:3.11-slim

# Create app directory
WORKDIR /src

# Install deps early (better caching)
COPY app/requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir -r /src/requirements.txt

# Copy the whole project so /src/app exists as a package
COPY . /src

RUN python app/train.py

# (Optional) make sure Python can see /src
ENV PYTHONPATH=/src

# Cloud Run will send traffic to this port; we’ll bind uvicorn to it
ENV PORT=8000

# Start FastAPI as a module: app.main:app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
