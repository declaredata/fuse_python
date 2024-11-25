from contextlib import contextmanager
from typing import Generator, Any
from fuse_bench.timing import get_timing
from fuse_python.session import session
from fuse_python.dataframe import DataFrame


@contextmanager
def sql_api(csv_file: str) -> Generator[tuple[DataFrame, float], Any, Any]:
    with session(
        host="localhost",
        port=8080,
        app_name="simplebench-sql",
    ) as fuse:

        def run() -> DataFrame:
            table_name = "simplebenchsql"
            df = fuse.read.csv(file_name=csv_file)
            df.write.saveAsTable(table_name)
            df = fuse.sql(query=f"SELECT * FROM {table_name}")
            # need this in place so that we actually process all the data
            # in the dataframe. otherwise we'll just end up timing the lazy
            # operations
            df.export_csv()
            return df

        yield get_timing(run)
