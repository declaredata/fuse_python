from contextlib import contextmanager
import os
from typing import Iterator

from declaredata_fuse.dataframe import DataFrame
from declaredata_fuse.session import session

@contextmanager
def setup_dataframe(test_name: str, file_name: str) -> Iterator[DataFrame]:
    host = os.getenv("FUSE_PYTHON_BENCH_HOST") or "localhost"
    port = int(os.getenv("FUSE_PYTHON_BENCH_PORT") or 8080)
    with session(
        host=host,
        port=port,
        app_name=test_name,
    ) as fuse:
        df = fuse.read.csv(file_name=file_name)
        yield df

