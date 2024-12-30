# Fuse benchmarking suite

This directory contains a benchmarking suite for the Fuse client library. To run it, ensure that you have a Fuse server running on `localhost:8080`, then run the following command from the root of this repository:

>See below for how to run a Fuse server on `localhost:8080`

```base
make run-bench
```

## Running a Fuse server on your local machine

The Fuse server is packaged as a Docker container, and pushed to [the `DeclareData` GitHub package repository](https://github.com/orgs/declaredata/packages/container/package/fuse).

To run it on your local machine, you need to have Docker installed. If you don't have Docker installed, see instructions for how to do so [here](https://docs.docker.com/get-docker/). Assuming you do have Docker installed, see the instructions below.

### Running on an `x64` (Intel) based machine

If you're on an Intel/x64-based machine, run the following command to start the Fuse server:

```bash
docker run --platform linux/amd64 -p 8080:8080 ghcr.io/declaredata/fuse:latest
```

### Running on an `arm64`-based machine

If you are using an Arm-based machine like a modern Mac with Apple Silicon, run the following command to start the Fuse server:

```bash
docker run --platform linux/arm64 -p 8080:8080 ghcr.io/declaredata/fuse:latest
```

### After Fuse is running

The above command will start the Fuse server on `localhost:8080`. Since the server listens for requests forever, it won't exit unless you force it to. Run the benchmarking suite (described above) in a new terminal window.
