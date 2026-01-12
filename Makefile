.PHONY: build publish dev init format lint lock test generate docs docs-clean

ifndef VERSION
VERSION := local
endif

.env: .env.example
	@echo "Creating API service .env file from template..."
	cp .env.example .env

clean:
	@echo "Cleaning up cache and build files..."
	rm -rf .mypy_cache .pytest_cache .ruff_cache .venv pytest.ini
	find . -name __pycache__ | xargs rm -rf

init:
	@echo "Installing dependencies..."
	poetry config virtualenvs.in-project true
	poetry env remove --all || true
	poetry install --no-root

build:
	@echo "Building package into dist/..."
	rm -rf dist
	@orig_version=$$(poetry version -s); \
	trap 'poetry version "'"$$orig_version"'" >/dev/null 2>&1 || true' EXIT; \
	if [ "$(VERSION)" != "local" ] && [ -n "$(VERSION)" ]; then \
		echo "Using VERSION=$(VERSION)"; \
		poetry version "$(VERSION)" >/dev/null; \
	fi; \
	poetry build

publish:
	@echo "Publishing package to PyPI..."
	@orig_version=$$(poetry version -s); \
	trap 'poetry version "'"$$orig_version"'" >/dev/null 2>&1 || true' EXIT; \
	if [ "$(VERSION)" != "local" ] && [ -n "$(VERSION)" ]; then \
		echo "Using VERSION=$(VERSION)"; \
		poetry version "$(VERSION)" >/dev/null; \
	fi; \
	poetry publish --build

format:
	@echo "Formatting code..."
	poetry run black .

lint:
	@echo "Running linting and formatting..."
	poetry run ruff check --fix .
	poetry run black .
	poetry run mypy .

lock:
	@echo "Locking dependencies..."
	poetry lock

test:
	@echo "Running tests..."
	poetry run pytest $(ARGS)

generate:
	@echo "Generating OpenAPI client into seclai/_generated..."
	poetry run openapi-python-client generate --meta none --path openapi/seclai.openapi.json --output-path seclai/_generated --overwrite

docs:
	@echo "Generating SDK documentation into build/docs..."
	@if [ "$(VERSION)" != "local" ] && [ -n "$(VERSION)" ]; then \
		echo "Building versioned docs: $(VERSION) (and latest)"; \
		rm -rf build/docs/$(VERSION) build/docs/latest; \
		mkdir -p build/docs/$(VERSION) build/docs/latest; \
		poetry run pdoc --output-directory build/docs/$(VERSION) seclai '!seclai\\._generated'; \
		poetry run pdoc --output-directory build/docs/latest seclai '!seclai\\._generated'; \
		printf '%s\n' \
			'<!doctype html>' \
			'<html>' \
			'  <head>' \
			'    <meta charset="utf-8" />' \
			'    <meta http-equiv="refresh" content="0; url=./latest/" />' \
			'    <meta name="viewport" content="width=device-width, initial-scale=1" />' \
			'    <title>Seclai Python SDK Docs</title>' \
			'  </head>' \
			'  <body>' \
			'    <p>Redirecting to <a href="./latest/">latest docs</a>…</p>' \
			'  </body>' \
			'</html>' \
			> build/docs/index.html; \
	else \
		mkdir -p build/docs; \
		poetry run pdoc --output-directory build/docs seclai '!seclai\\._generated'; \
	fi

docs-clean:
	@echo "Removing generated docs..."
	rm -rf build/docs
