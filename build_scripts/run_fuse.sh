#!/bin/bash

set -eo pipefail

run_fuse() {
    TAG=${1:-latest}
    IMAGE=ghcr.io/declaredata/fuse:${TAG}
    echo "running Fuse server: ${IMAGE}"
    docker run \
        -p 8080:8080 \
        -v "$(pwd)/datasets:/datasets" \
        "${IMAGE}"
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    run_fuse "$@"
fi
