# DeclareData Fuse Client Bindings for Python

This is the client library for the DeclareData Fuse Server. It provides an API very similar to and compatible with the pyspark API, but connects to a proprietary server (called `fuse-server`) that can be quickly downloaded.

The API is documented in two ways:

- Basic Python documentation is included under the `fuse_python` directory
- Several usage examples are included in the `fuse_bench` directory

See below for information on installing dependencies and running the server.

## Getting the server

The server is a single self-contained binary which you can download using the following `curl` command:

```shell
curl -o /usr/local/bin/fuse-server -L https://declaredata-test.sfo3.cdn.digitaloceanspaces.com/
chmod +x /usr/local/bin/fuse_server
```

When you're ready to run the server, do so with this command:

```shell
RUST_LOG=info /usr/local/bin/fuse_server
```

Once started, the server will listen on port 8080 and hang until you close it with `ctrl+C`. Make sure you keep it running in a separate tab or window while you work.

## Installing the library

The client bindings are located in this repository at [`./fuse_python`](./fuse_python/), and are published to PyPI as both a wheel and source distribution. Install them using the following command:


```shell
pip install declaredata_fuse
```
