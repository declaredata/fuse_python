#!/bin/bash

set -eo pipefail

run_bench() {
    # uv run python bench/src/bench/main.py
	cd bench && uv run pytest
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    run_bench "$@"
fi
