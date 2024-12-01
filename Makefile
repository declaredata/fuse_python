.PHONY: gen-proto
gen-proto:
	buf generate

.PHONY: ruff-python
ruff:
	uv run ruff check
	uv run ruff format

.PHONY: pyright
pyright:
	uv run pyright ./fuse_python
	uv run pyright ./fuse_bench

.PHONY: run-bench
run-bench:
	uv run python fuse_bench/src/fuse_bench/main.py

.PHONY: .run-bench-verbose
run-bench-verbose:
	uv run python fuse_bench/src/fuse_bench/main.py --verbose true

.PHONY: build-release
build-release:
	rm -r ./dist
	uv build --project fuse_python --sdist --wheel

.PHONY: publish-release
publish-release: build-release
	uv publish dist/*
