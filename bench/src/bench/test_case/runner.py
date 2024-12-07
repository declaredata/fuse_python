from dataclasses import dataclass
from typing import Callable
from bench.timing import get_timing
from declaredata_fuse.dataframe import DataFrame
from declaredata_fuse.session import session


@dataclass
class TestCase:
    test_name: str
    file_name: str
    runner: Callable[[DataFrame], DataFrame]
    verbose: bool
    host: str = "localhost"
    port: int = 8080


def run_df_test_case(tc: TestCase):
    print(f"Starting {tc.test_name} test")
    with session(
        host=tc.host,
        port=tc.port,
        app_name=tc.test_name,
    ) as fuse:
        df = fuse.read.csv(file_name=tc.file_name)

        def func_to_time() -> DataFrame:
            new_df = tc.runner(df)
            # make sure we collect here so that the server is forced
            # to actually eagerly process the data. if we don't do this,
            # we'll end up just timing the lazy construction of the new
            # dataframe
            new_df.collect()
            return new_df

        new_df, elapsed = get_timing(func=func_to_time)
        if tc.verbose:
            new_df.limit(0, 10).display()
        print(f"[{tc.test_name}] took {elapsed} sec")
