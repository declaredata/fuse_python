# Fuse benchmarking suite

This directory contains a benchmarking suite for the Fuse client library. To run it, ensure that you have a Fuse server running on `localhost:8080`, then run the following command from the root of this repository:

>See below for how to run a Fuse server on `localhost:8080`

```base
make run-bench
```

## Running a Fuse server on your local machine

The Fuse server is packaged as a Docker container, and pushed to [the `DeclareData` GitHub package repository](https://github.com/orgs/declaredata/packages/container/package/fuse).

To run it on your local machine, you need to have Docker installed. If you don't have Docker installed, see instructions for how to do so [here](https://docs.docker.com/get-docker/). Assuming you do have Docker installed, run the Fuse server with the following command (from the root of this repository):

```bash
make run-fuse
```

### Customizing this command

This command runs the Fuse server with some default settings. You can customize it by setting the following environment variables:

- `FUSE_FOLLOW_LOGS` - Set to `true` to follow the logs of the Fuse server as it runs. Default is `false`.
  - If you set this to `true`, logs will stream in your terminal window and never exit until you press `ctrl+c`. Doing so will not stop the server, however.
- `FUSE_PLATFORM` - The Fuse server is built for `linux/amd64` and `linux/arm64`. This variable lets you specify which platform to run the server on. Default is `linux/amd64`.

### After Fuse is running

The above command will start the Fuse server on `localhost:8080`. Since the server listens for requests forever, it won't exit unless you force it to. Run the benchmarking suite (described above) in a new terminal window.
