from contextlib import contextmanager
from typing import Generator, Any
from bench.timing import get_timing
from declaredata_fuse.row import Row
from declaredata_fuse.session import session


@contextmanager
def df_collect(csv_file: str) -> Generator[tuple[list[Row], float], Any, Any]:
    with session(
        host="localhost",
        port=8080,
        app_name="simplebench-df",
    ) as fuse:

        def run():
            return fuse.read.csv(file_name=csv_file).limit(0, 1000).collect()

        yield get_timing(run)
