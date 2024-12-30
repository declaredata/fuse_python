#!/bin/bash

set -eo pipefail

run_fuse() {
    TAG=$(cat ci_bench_image_sha)
    PLATFORM="linux/amd64"
    IMAGE=ghcr.io/declaredata/fuse:${TAG}
    echo "running Fuse server: ${IMAGE} with platform ${PLATFORM}"
    CONTAINER_ID=$(docker run \
        -d \
        -p 8080:8080 \
        --platform ${PLATFORM} \
        -v "$(pwd)/datasets:/datasets" \
        "${IMAGE}")
    echo "Container ID: ${CONTAINER_ID}"
    docker logs -f ${CONTAINER_ID}
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    run_fuse "$@"
fi
