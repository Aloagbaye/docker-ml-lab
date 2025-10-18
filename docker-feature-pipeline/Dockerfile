FROM python:3.11-slim
WORKDIR /app

# System deps (psycopg2 compilation + curl)
RUN apt-get update && apt-get install -y gcc libpq-dev curl && rm -rf /var/lib/apt/lists/*

# Python libs for data + Feast + Postgres + Redis
RUN pip install --no-cache-dir \
    jupyterlab numpy pandas sqlalchemy psycopg2-binary \
    feast==0.42.0 redis==5.0.1

EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
