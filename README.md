# DeclareData Fuse Client Bindings for Python

This is the python client library for the **DeclareData Fuse Server**. It provides an API very similar to and compatible with the pyspark API, but connects to a proprietary server (called `fuse-server`) that can be quickly downloaded.

> [!NOTE]
>
> **DeclareData** is under active development. This is a pre-release version and may contain bugs, incomplete features or other issues. Also, please review and add to the latest [open compatibility development status](https://github.com/declaredata/fuse_python/issues/6).

## Prerequisites

Before installing DeclareData Fuse, ensure you have the following:
- Python 3.10+
- At least 8GB of available memory
- pip package manager
- Docker (if using Docker method)
- curl (for downloading the server binary if using direct method)
- Port 8080 available on your machine (future versions will allow changing the port)

## Getting and Running the Server

There are two methods to set up and run the DeclareData Fuse server:

### Method 1: Docker Container (Recommended)

Run the server using Docker:
```shell
docker run 021939395539.dkr.ecr.us-west-1.amazonaws.com/declaredata_fuse:1b70474
```

> [!EXPERIMENTAL]
> There is an experimental single install script command for MacOS/Linux that will download the server and run it in a Docker container: `curl -LsSf https://declaredata.com/fuse/install.sh | sh`

### Method 2: Direct Binary Download

Download and run the server using curl:
```shell
# Download the server
curl -o ./fuse_server -L https://declaredata-test.sfo3.cdn.digitaloceanspaces.com/fuse-server
chmod +x ./fuse_server

# Run the server
RUST_LOG=info ./fuse_server
```

Once started, the server will listen on port 8080 and hang until you close it with `ctrl+C`. Make sure you keep it running in a separate tab or window while you work.

## Installing the Library

The client bindings are located in this repository at [`./declaredata_fuse`](./declaredata_fuse/), and are [published to PyPI](https://pypi.org/project/declaredata_fuse/#description) as both a wheel and source distribution. Install them using the following command:

```shell
pip install declaredata_fuse
```

Update the library using the following command:

```shell
pip install --upgrade declaredata_fuse
```

## Documentation

The API is documented in two ways:
- Basic Python documentation is included under the `declaredata_fuse` directory
- Several usage examples are included in the `bench` directory

## Basic Usage

The first step to using the library is to import it and create a `FuseSession` instance:

```python
from declaredata_fuse.session import FuseSession
# assumes the server is running on localhost:8080
fs = FuseSession.builder.getOrCreate()
```

Then, you can read data from a CSV file and show a little bit of data:

```python
df = fs.read.csv("data.csv")
df.show(10)
```

>Note: you can read CSV, Parquet and JSON files from local files or remote sources like S3 or DigitalOcean Spaces.

You can also do some basic operations like filtering and sorting:

```python
# get all rows from 2000 to modern day
df.filter(df.year >= 2000).show(10)
# sort rows by highest to lowest population, then show the
# top 10 rows
df.sort(
    df.population, ascending=False,
).select(
    df.year, df.state_abbr, df.population,
).show(10)
```

And finally, let's put it all together with some grouping and aggregating:

```python
import declaredata_fuse.functions as F
df.groupBy("year").agg(
    F.first("population").alias("highest_population_of_year"),
).sort(df.highest_population_of_year, ascending=False).show(10)
```

## Submitting Issues

If you encounter any problems while using DeclareData Fuse, please submit an issue on our GitHub repository:

1. Go to the [Issues](https://github.com/declaredata/fuse_python/issues) tab
2. Click "New Issue"
3. Feel free to use our issue template below to provide:
   - Description of the problem
   - Steps to reproduce
   - Expected behavior
   - Actual behavior
   - Environment details (OS, Python version, etc.)
   - Relevant error messages or logs

For security-related issues, please email us.
