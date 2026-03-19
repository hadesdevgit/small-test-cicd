# small-test-cicd

Small sample project with a minimal CI/CD pipeline.

## What it does
- A tiny Python module (`cicd_sample`) with a simple function.
- Tests with `pytest`.
- Lint + format checks with `ruff`.
- Docker image build.

## Local dev

### Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
```

### Run checks
```bash
ruff check .
ruff format --check .
pytest -q
```

### Run the demo
```bash
python -m cicd_sample
```

### Build Docker image
```bash
docker build -t cicd-sample:local .
docker run --rm cicd-sample:local
```

### One-command dev
```bash
make dev
```

## GitHub Actions
- **CI**: runs on pushes and PRs, executes lint/format/tests and builds the Docker image.
- **CD**: on pushes to `main` and on version tags (`v*`), publishes a Docker image to GitHub Container Registry (GHCR) as `ghcr.io/<owner>/<repo>`.

