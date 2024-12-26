r"""
# PySpark API for DeclareData Fuse Server

A Python client library for **DeclareData Fuse Server** that provides a PySpark-compatible API. Scale down your Apache Spark clusters and speed up workloads without changing your code.

# Prerequisites

* Python 3.10 or higher
* 8GB+ available memory
* pip package manager
* Docker (for container deployment)
* Available port 8080 (port customization coming in future versions)

# Components

* [**DeclareData Fuse Server**](#server-setup): Fast, low-overhead drop-in alternative to Apache Spark
* [**DeclareData Fuse Python**](#python-client-installation): Python client library providing PySpark-compatible APIs

# Server Setup

Run the Fuse server using Docker:

```bash
docker run -p 8080:8080 ghcr.io/declaredata/fuse:latest
```

> **Note:** All images are published to our GitHub Package Docker repository, which can be found at [DeclareData Fuse Packages](https://github.com/orgs/declaredata/packages/container/package/fuse).

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

# Python Client Installation

Install from PyPI:

```bash
pip install declaredata_fuse
```

Update to the latest version:

```bash
pip install --upgrade declaredata_fuse
```

# Quick Start Guide

## Initialize a Session

```python
from declaredata_fuse.session import FuseSession

# Connect to DeclareData Fuse Server (default: localhost:8080)
fs = FuseSession.builder.getOrCreate()
```

## Basic Data Operations

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
"""

from declaredata_fuse import column
from declaredata_fuse import column_abc
from declaredata_fuse import column_alias
from declaredata_fuse import column_coalesce
from declaredata_fuse import column_filter
from declaredata_fuse import column_functional
from declaredata_fuse import column_literal
from declaredata_fuse import column_op
from declaredata_fuse import column_or_name
from declaredata_fuse import dataframe
from declaredata_fuse import dataframe_impl
from declaredata_fuse import functions
from declaredata_fuse import grouped
from declaredata_fuse import row
from declaredata_fuse import session
from declaredata_fuse import window

__all__ = [
    "column",
    "column_abc",
    "column_alias",
    "column_coalesce",
    "column_filter",
    "column_functional",
    "column_literal",
    "column_op",
    "column_or_name",
    "dataframe",
    "dataframe_impl",
    "functions",
    "grouped",
    "row",
    "session",
    "window",
]

__version__ = "0.1.0"  # Add version if you haven't already
