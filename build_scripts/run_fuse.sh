#!/bin/bash

set -eo pipefail

run_fuse() {
    FOLLOW_LOGS=${1:-false}
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

    if [ "${FOLLOW_LOGS}" = "true" ]; then
        echo "container ${CONTAINER_ID} started. following logs"
        docker logs -f ${CONTAINER_ID}
    else
        echo "container ${CONTAINER_ID} started. not following logs"
        docker logs ${CONTAINER_ID}
    fi
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    run_fuse "$@"
fi
