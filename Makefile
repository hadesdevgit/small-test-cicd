.PHONY: venv dev lint fmt test run docker-build

venv:
	python3 -m venv .venv

dev: venv
	. .venv/bin/activate && python -m pip install -U pip && pip install -r requirements.txt && pip install -e .

lint:
	. .venv/bin/activate && ruff check .

fmt:
	. .venv/bin/activate && ruff format --check .

test:
	. .venv/bin/activate && pytest -q

run:
	. .venv/bin/activate && python -m cicd_sample

docker-build:
	docker build -t cicd-sample:local .

