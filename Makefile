.PHONY: gen-proto
gen-proto:
	buf generate

.PHONY: ruff-python
ruff:
	uv run ruff check
	uv run ruff format

.PHONY: pyright
pyright:
	uv run pyright ./declaredata_fuse
	uv run pyright ./bench

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
