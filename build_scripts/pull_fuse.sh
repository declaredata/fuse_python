#!/bin/bash

set -eo pipefail

pull_fuse() {
    TAG=$(cat ci_bench_image_sha)
    PLATFORM="linux/amd64"
    IMAGE=ghcr.io/declaredata/fuse:${TAG}
    echo "pulling Fuse server: ${IMAGE} with platform ${PLATFORM}"
    docker pull --platform ${PLATFORM} ${IMAGE}
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    pull_fuse "$@"
fi
