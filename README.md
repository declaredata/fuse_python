> DeclareData is under active development. This is a pre-release version and may contain bugs or incomplete features. Please review and contribute to our [compatibility development status](https://github.com/declaredata/fuse_python/issues/6).

<div align="left">
  <a href="https://declaredata.com">
  <picture>
    <img width="150px" src="https://github.com/user-attachments/assets/ef5a2273-2cf1-46be-ab4a-6ddc6c99705e" alt="DeclareData Logo">
  </picture>
  </a>
</div>

<div>

[![PyPI - Version](https://img.shields.io/pypi/v/declaredata_fuse?label=PyPi%20Release&color=7E22CE)](https://pypi.org/project/declaredata_fuse/)
![Python Version](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/declaredata/fuse_python/refs/heads/main/pyproject.toml&label=Python%20Version&color=7E22CE)
[![License](https://img.shields.io/github/license/declaredata/fuse_python.svg?label=License&color=7E22CE)](https://github.com/declaredata/fuse_python/blob/main/LICENSE)
[![CI](https://github.com/declaredata/fuse_python/actions/workflows/python.yml/badge.svg?branch=main)](https://github.com/declaredata/fuse_python/actions)
[![Benchmark](https://github.com/declaredata/fuse_python/actions/workflows/bench.yml/badge.svg?branch=main&color=7E22CE)](https://github.com/declaredata/fuse_python/actions)

</div>

# DeclareData Fuse Client Bindings for Python

A Python client library for **DeclareData Fuse Server** that provides a PySpark-compatible API. Scale down your Spark clusters and speed up workloads without changing your code.

# Contents

- [Prerequisites](#prerequisites)
- [Components](#components)
- [Server Setup](#server-setup)
- [Python Client Installation](#python-client-installation)
- [Quick Start Guide](#quick-start-guide)
  - [Initialize a Session](#initialize-a-session)
  - [Basic Data Operations](#basic-data-operations)
- [Other Documentation 🚧 WIP](#other-documentation--wip)
- [Issue Reporting](#issue-reporting)

# Prerequisites

* Python 3.10 or higher
* 8GB+ available memory
* pip package manager
* Docker
* Available port 8080 (required for gRPC) and port 3000 (optional for web interface)

# Components

* [**DeclareData Fuse Server**](#server-setup): Blazing fast, low-overhead drop-in alternative to Apache Spark clusters that runs anywhere
* [**DeclareData Fuse Python**](#python-client-installation): Python client library providing PySpark-compatible APIs

# Server Setup

Run the Fuse server using Docker:

```bash
docker run -p 8080:8080 -p 3000:3000 ghcr.io/declaredata/fuse:latest
```

> **Note:** All images are published to our GitHub Package Docker repository, which can be found at [github.com/orgs/declaredata/packages/container/package/fuse](https://github.com/orgs/declaredata/packages/container/package/fuse).

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

# Other Documentation 🚧 WIP

* Additional API documentation is also available [`here`](https://docs.declaredata.com)
* Usage examples can be found in the [`bench`](./bench/) directory

# Issue Reporting

Please report issues via our [GitHub Issues](https://github.com/declaredata/fuse_python/issues) page with the following information:

* Problem description
* Steps to reproduce
* Expected vs actual behavior
* Environment details (OS, Python version)
* Error messages or logs

For security concerns, please email us directly.
