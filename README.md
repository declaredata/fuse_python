> DeclareData is under active development. This is a pre-release version and may contain bugs or incomplete features. Please review and contribute to our [compatibility development status](https://github.com/declaredata/fuse_python/issues/6).

# DeclareData Fuse Client Bindings for Python

A Python client library for **DeclareData Fuse Server** that provides a PySpark-compatible API. Scale down your Spark clusters and speed up workloads without changing your code.

## Contents

* [Prerequisites](#prerequisites)
* [Components](#components)
* [Server Setup](#server-setup)
* [Python Client Installation](#python-client-installation)
* [Quick Start Guide](#quick-start-guide)
* [Issue Reporting](#issue-reporting)

## Prerequisites

* Python 3.10 or higher
* 8GB+ available memory
* pip package manager
* Docker (for container deployment)
* curl (for binary download)
* Available port 8080 (port customization coming in future versions)

## Components

* [**DeclareData Fuse Server**](#server-setup): Blazing fast, low-overhead drop-in alternative to Apache Spark clusters that runs anywhere
* [**DeclareData Fuse Python**](#python-client-installation): Python client library providing PySpark-compatible APIs

## Server Setup

Run the Fuse server using Docker:

```bash
docker run -p 8080:8080 021939395539.dkr.ecr.us-west-1.amazonaws.com/declaredata_fuse:187c3118082527ce2796785d5aab00b8f09e8290
```

> **Note:** Currently requires AWS account access to pull from ECR. Broader availability coming soon.

<!--
### Method 2: Direct Binary Download

```bash
# Download the DeclareData Fuse Server
curl -o ./fuse_server -L https://declaredata-test.sfo3.cdn.digitaloceanspaces.com/fuse-server
chmod +x ./fuse_server

# Run the DeclareData Fuse Server
RUST_LOG=info ./fuse_server
```

### Method 3: Experimental One-Line Install (MacOS/Linux)

```bash
curl -LsSf https://declaredata.com/fuse/install.sh | sh
```

This script downloads the Docker image and installs the DeclareData Fuse Python client library automatically.
-->

## Python Client Installation

Install from PyPI:

```bash
pip install declaredata_fuse
```

Update to the latest version:

```bash
pip install --upgrade declaredata_fuse
```

## Quick Start Guide

### Initialize a Session

```python
from declaredata_fuse.session import FuseSession

# Connect to DeclareData Fuse Server (default: localhost:8080)
fs = FuseSession.builder.getOrCreate()
```

### Basic Data Operations

```python
# Read CSV file
df = fs.read.csv("data.csv")
df.show(10)

# Filter data
df.filter(df.year >= 2000).show(10)

# Sort and select columns
df.sort(
    df.population, ascending=False
).select(
    df.year, df.state_abbr, df.population
).show(10)

# Group and aggregate
import declaredata_fuse.functions as F

df.groupBy("year").agg(
    F.first("population").alias("highest_population_of_year")
).sort(
    df.highest_population_of_year, ascending=False
).show(10)
```

## Other Documentation 🚧 WIP

* API documentation is available in the [`declaredata_fuse`](./declaredata_fuse/) directory
* Usage examples can be found in the [`bench`](./bench/) directory

## Issue Reporting

Please report issues via our [GitHub Issues](https://github.com/declaredata/fuse_python/issues) page with the following information:

* Problem description
* Steps to reproduce
* Expected vs actual behavior
* Environment details (OS, Python version)
* Error messages or logs

For security concerns, please email us directly.
