# \# \*\*docker-ml-lab\*\*

# 

# Reproducible, containerized labs for end-to-end Machine Learning:

# 

# \* spin up a local ML workspace,

# 

# \* run a simple training/inference pipeline,

# 

# \* and experiment with experiment tracking via MLflow.

# 

# Repo layout:

# 

# \* `docker-feature-pipeline/` – feature engineering lab (Dockerfile \\+ Compose).

# 

# \* `docker-ml-pipeline/` – training/inference pipeline lab (Dockerfile \\+ Compose).

# 

# \* `docker-mlflow-lab/` – MLflow tracking server lab (Compose).

# 

# \* `notebooks/` – example notebooks you can bind-mount into the labs. \[GitHub](https://github.com/Aloagbaye/docker-ml-lab)

# 

# ---

# 

# \## \*\*Table of contents\*\*

# 

# \* Quick start

# 

# \* Prerequisites

# 

# \* What’s inside

# 

# \* Usage by lab

# 

# &nbsp; \* Feature Pipeline Lab

# 

# &nbsp; \* ML Pipeline Lab

# 

# &nbsp; \* MLflow Lab

# 

# \* Volumes \& data

# 

# \* GPU (optional)

# 

# \* Troubleshooting

# 

# \* FAQ

# 

# \* License

# 

# ---

# 

# \## \*\*Quick start\*\*

# 

# `# 1) Clone`  

# `git clone https://github.com/Aloagbaye/docker-ml-lab.git`  

# `cd docker-ml-lab`

# 

# `# 2) Pick a lab and run it (examples below)`  

# `cd docker-ml-pipeline`  

# `docker compose up --build`

# 

# Then open the printed URL(s)—typically something like:

# 

# \* app / API: \[http://localhost:8000](http://localhost:8000) or \[http://localhost:8080](http://localhost:8080)

# 

# \* Jupyter: \[http://localhost:8888](http://localhost:8888)

# 

# \* MLflow UI: \[http://localhost:5000](http://localhost:5000)

# 

# (See each lab’s section for exact endpoints/ports.)

# 

# ---

# 

# \## \*\*Prerequisites\*\*

# 

# \* Docker Desktop (or Docker Engine) 24+ and Docker Compose v2

# 

# \* \\~6–8 GB RAM free recommended when running multiple services

# 

# \* (Optional) NVIDIA GPU drivers \\+ `nvidia-container-toolkit` for GPU compute

# 

# ---

# 

# \## \*\*What’s inside\*\*

# 

# Each lab is self-contained with its own `Dockerfile` and/or `docker-compose.yml`.

# 

# \### \*\*Common conventions\*\*

# 

# \* \*\*Images\*\*: built from local Dockerfiles where provided.

# 

# \* \*\*Ports\*\*: published to `localhost` for easy access.

# 

# \* \*\*Dev volumes\*\*: local `notebooks/` and `data/` folders can be mounted for live editing.

# 

# \* \*\*.env\*\*: you can add per-lab `.env` files to override ports and paths.

# 

# ---

# 

# \## \*\*Usage by lab\*\*

# 

# \### \*\*Feature Pipeline Lab\*\*

# 

# Folder: `docker-feature-pipeline/` \[GitHub](https://github.com/Aloagbaye/docker-ml-lab)

# 

# \*\*Goal:\*\* Explore feature engineering and data preparation in an isolated container.

# 

# \*\*Run:\*\*

# 

# `cd docker-feature-pipeline`  

# `# If a compose file exists:`  

# `docker compose up --build`  

# `# Otherwise, build/run directly:`  

# `docker build -t feature-pipeline .`  

# `docker run --rm -p 8888:8888 -v "$PWD/../notebooks":/workspace/notebooks feature-pipeline`

# 

# \*\*Typical endpoints (example):\*\*

# 

# \* Jupyter: \[http://localhost:8888](http://localhost:8888) (token shown in container logs)

# 

# Tip: Mount your local `notebooks/` so edits persist.

# 

# ---

# 

# \### \*\*ML Pipeline Lab\*\*

# 

# Folder: `docker-ml-pipeline/` \[GitHub](https://github.com/Aloagbaye/docker-ml-lab)

# 

# \*\*Goal:\*\* Train and/or serve a simple ML model with a predictable, reproducible stack (e.g., FastAPI \\+ joblib model, or a CLI runner).

# 

# \*\*Run:\*\*

# 

# `cd docker-ml-pipeline`  

# `docker compose up --build`

# 

# \*\*Typical endpoints (examples):\*\*

# 

# \* API / web app: \[http://localhost:8000](http://localhost:8000) (or 8080\\)

# 

# \* Docs (if FastAPI): \[http://localhost:8000/docs](http://localhost:8000/docs)

# 

# \*\*Common dev loop:\*\*

# 

# 1\. Edit code or notebook locally.

# 

# 2\. Rebuild: `docker compose build` (or use bind mounts for hot-reload).

# 

# 3\. Rerun: `docker compose up`.

# 

# ---

# 

# \### \*\*MLflow Lab\*\*

# 

# Folder: `docker-mlflow-lab/` \[GitHub](https://github.com/Aloagbaye/docker-ml-lab)

# 

# \*\*Goal:\*\* Bring up an \*\*MLflow Tracking Server\*\* locally (often alongside a backend store like Postgres and an artifact store like MinIO or a mounted volume).

# 

# \*\*Run:\*\*

# 

# `cd docker-mlflow-lab`  

# `docker compose up -d`

# 

# \*\*Typical endpoints (examples):\*\*

# 

# \* MLflow UI: \[http://localhost:5000](http://localhost:5000)

# 

# \* MinIO Console: \[http://localhost:9001](http://localhost:9001) (if used)

# 

# \* MinIO S3 endpoint: \[http://localhost:9000](http://localhost:9000) (if used)

# 

# \* Postgres: `localhost:5432` (internal only, via service name in Compose)

# 

# \*\*Point your code to MLflow:\*\*

# 

# `export MLFLOW\_TRACKING\_URI="http://127.0.0.1:5000"`  

# `# or use the service name inside the Compose network when calling from another container`

# 

# If the lab includes MinIO, set AWS-style creds via `.env` (e.g., `MINIO\_ROOT\_USER`, `MINIO\_ROOT\_PASSWORD`) and configure MLflow’s artifact store accordingly.

# 

# ---

# 

# \## \*\*Volumes \& data\*\*

# 

# \* \*\*`./notebooks/`\*\*: mount into containers at `/workspace/notebooks` (or similar) for persistence.

# 

# \* \*\*`./data/`\*\* (create as needed): mount to `/workspace/data` for datasets and artifacts.

# 

# \* \*\*MLflow artifacts\*\*: if MinIO is included, they’re stored in the configured S3 bucket; if not, they may be on a local volume.

# 

# \*\*Cleaning up:\*\*

# 

# `# Stop and remove containers but keep volumes (fast restart)`  

# `docker compose down`

# 

# `# Stop and remove everything including volumes (fresh reset)`  

# `docker compose down -v`

# 

# ---

# 

# \## \*\*GPU (optional)\*\*

# 

# If you want to use CUDA:

# 

# 1\. Install \*\*NVIDIA drivers\*\* and \*\*nvidia-container-toolkit\*\* on the host.

# 

# Add the following to your service in `docker-compose.yml`:

# 

# &nbsp;`deploy:`  

# &nbsp; `resources:`  

# &nbsp;   `reservations:`  

# &nbsp;     `devices:`  

# &nbsp;       `- capabilities: \["gpu"]`

# 

# 2\. 

# 

# Run with GPU access, e.g.:

# 

# &nbsp;`docker compose up --build`

# 

# 3\.  (On some setups you may need `--gpus all` in a `docker run` scenario.)

# 

# ---

# 

# \## \*\*Troubleshooting\*\*

# 

# \* \*\*Port already in use\*\*  

# &nbsp;  Change the published port in the lab’s `docker-compose.yml` (e.g., `5000:5000` → `5500:5000`) and restart.

# 

# \* \*\*Can’t reach the UI\*\*  

# &nbsp;  Confirm the container is healthy: `docker ps` → check `STATUS`. Then `docker logs <service>` for the token/URL.

# 

# \* \*\*Pip install / dependency errors\*\*  

# &nbsp;  Rebuild without cache: `docker compose build --no-cache` to pick up updated `requirements.txt`.

# 

# \* \*\*MLflow can’t write artifacts\*\*  

# &nbsp;  If using MinIO, verify credentials, bucket name, and endpoint URL; ensure the service is up in Compose.

# 

# \* \*\*Windows paths\*\*  

# &nbsp;  Use absolute paths or WSL2. For bind mounts in `docker-compose.yml`, prefer relative paths from the lab folder.

# 

# ---

# 

# \## \*\*FAQ\*\*

# 

# \*\*Q: Where do I put my own notebooks?\*\*  

# &nbsp;A: In `./notebooks/`. They’ll appear inside the container at the mounted path.

# 

# \*\*Q: Can I point the ML pipeline lab at the MLflow tracking server?\*\*  

# &nbsp;A: Yes—start `docker-mlflow-lab` first, then set `MLFLOW\_TRACKING\_URI` and any artifact store env vars in the pipeline lab.

# 

# \*\*Q: Can I run all labs at once?\*\*  

# &nbsp;A: You can, but mind the ports. Either change published ports per lab or start them one at a time.

# 

# ---

# 

# \## \*\*License\*\*

# 

# MIT (or your preferred license—update this section).

# 

# ---

# 

# \### \*\*Maintainer\*\*

# 

# \*\*Israel Igietsemhe (Aloagbaye)\*\*  

# &nbsp;If you find issues or want enhancements, open an issue or PR.

# 



