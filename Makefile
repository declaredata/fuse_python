.PHONY: gen-proto
gen-proto:
	buf generate

check: ruff typecheck test

.PHONY: ruff-python
ruff:
	uv run ruff check
	uv run ruff format


.PHONY: pyright
typecheck:
	cd declaredata_fuse && uv run pyright

.PHONY: test
test:
	cd declaredata_fuse && uv run pytest
	cd bench && uv run pytest

.PHONY: run-bench
run-bench:
	uv run python bench/src/bench/main.py

.PHONY: .run-bench-verbose
run-bench-verbose:
	uv run python bench/src/bench/main.py --verbose true

.PHONY: build-release
build-release:
	rm -rf ./dist
	uv build --project declaredata_fuse --sdist --wheel

.PHONY: publish-release
publish-release: build-release
	uv publish dist/*
