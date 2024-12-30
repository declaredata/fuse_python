.PHONY: check
check: ruff typecheck test

.PHONY: gen-proto
gen-proto:
	buf generate

.PHONY: ruff-python
ruff:
	uv run ruff check
	uv run ruff format

.PHONY: pyright
typecheck:
	cd declaredata_fuse && uv run pyright
	cd bench && uv run pyright

.PHONY: test
test:
	cd declaredata_fuse && uv run pytest

.PHONY: run-bench
run-bench:
	./build_scripts/run_bench.sh

.PHONY: .run-bench-verbose
run-bench-verbose:
	uv run python bench/src/bench/main.py --verbose true
	cd bench && uv run pytest

.PHONY: pull-fuse
pull-fuse:
	./build_scripts/pull_fuse.sh

.PHONY: run-fuse
run-fuse:
	./build_scripts/run_fuse.sh false

.PHONY: build-release
build-release:
	rm -rf ./dist
	uv build --project declaredata_fuse --sdist --wheel

.PHONY: publish-release
publish-release: build-release
	uv publish dist/*
