# small-test-cicd

Small sample project with a minimal CI/CD pipeline.

## What it does
- A tiny Python module (`cicd_sample`) with a simple function.
- A tiny public HTTP API (FastAPI) exposing `GET /add?a=2&b=3 -> {"result": 5}`.
- Tests with `pytest`.
- Lint + format checks with `ruff`.
- Docker image build (runs the API via Uvicorn).

## Local dev

### Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
pip install -e .
```

### Run checks
```bash
ruff check .
ruff format --check .
pytest -q
```

### Run the CLI demo
```bash
python -m cicd_sample
```

### Run the API locally
```bash
uvicorn cicd_sample.api:app --reload --host 0.0.0.0 --port 8000
```

Then:

```bash
curl "http://localhost:8000/add?a=2&b=3"
```

### Build Docker image
```bash
docker build -t cicd-sample:local .
docker run --rm -p 8000:8000 cicd-sample:local
```

### One-command dev
```bash
make dev
```

## GitHub Actions
- **CI**: runs on PRs and pushes; executes lint/format/tests and builds the Docker image.
- **CD (GHCR)**: on pushes to `main` and on version tags (`v*`), publishes a Docker image to GitHub Container Registry (GHCR) as `ghcr.io/<owner>/<repo>`.
- **CD (Render)**: on pushes to `main`, triggers a Render deploy hook (see below).

## Render deployment (public)
This repo includes a `render.yaml` for a Docker-based Web Service.

### Setup
- Create a **Render Web Service** from this repo (Docker runtime).
- Create a **Deploy Hook** in Render.
- In GitHub repo settings, add an Actions secret:
  - **`RENDER_DEPLOY_HOOK`**: the full deploy hook URL from Render.

After that, every push to `main` will trigger a Render deploy via GitHub Actions.

