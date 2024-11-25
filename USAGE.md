# Using the client bindings

These bindings provide an interface very similar to the `pyspark` API, but connect to a proprietary server -- called `fuse-server` -- rather than Spark. Like Spark, the server does most of the "heavy lifting", and the client bindings simply orchestrate the work via remote calls (RPCs).

Unlike Spark, however, `fuse-server` is a single self-contained binary that can be downloaded and run with a single command. The server is written in Rust, and is much faster and more efficient than Spark, when run against small or moderate-sized datasets (<=5TB).
