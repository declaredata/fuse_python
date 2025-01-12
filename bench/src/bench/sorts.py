from contextlib import contextmanager
from typing import Any, Generator
from bench.test_case import TestCaseResult
from bench.timing import get_timing
from declaredata_fuse.dataframe import DataFrame
from declaredata_fuse.session import session
from declaredata_fuse.column.sorted import SortDirection, SortedColumn
from declaredata_fuse.condition import Condition
import declaredata_fuse.functions as F


@contextmanager
def sorts_api(csv_file: str) -> Generator[tuple[list[TestCaseResult], float], Any, Any]:
    with session(
        host="localhost",
        port=8080,
        app_name="simplebench-df",
    ) as fuse:

        def run():
            df = fuse.read.csv(file_name=csv_file)
            test_cases = cases(df)
            # need this in place so that we actually process all the data
            # in the dataframe. otherwise we'll just end up timing the lazy
            # operations
            for tc in test_cases:
                tc.dataframe.export_csv()
            return test_cases

        yield get_timing(run)


def cases(orig_df: DataFrame) -> list[TestCaseResult]:
    ret: list[TestCaseResult] = []

    # sort by year ascending
    year_col = F.col("year")
    sorted_df = orig_df.sort_typed(cols=[SortedColumn(year_col, SortDirection.ASC)])
    ret.append(
        TestCaseResult(description="sort by year ascending", dataframe=sorted_df)
    )

    # filter California only
    state_col = F.col("state_abbr")
    condition = Condition(state_col, "==", "CA")
    filtered_df = orig_df.filter(condition)
    ret.append(
        TestCaseResult(description="filter California only", dataframe=filtered_df)
    )

    # sort by violent crime descending
    crime_col = F.col("violent_crime")
    sorted_df = orig_df.sort_typed(cols=[SortedColumn(crime_col, SortDirection.DESC)])
    ret.append(
        TestCaseResult(
            description="sort by violent crime descending", dataframe=sorted_df
        )
    )

    # filter years > 2010
    year_col = F.col("year")
    condition = Condition(year_col, ">", 2010)
    filtered_df = orig_df.filter(condition)
    ret.append(TestCaseResult(description="filter years > 2010", dataframe=filtered_df))

    # sort by property crime ascending
    crime_col = F.col("property_crime")
    sorted_df = orig_df.sort_typed(cols=[SortedColumn(crime_col, SortDirection.ASC)])
    ret.append(
        TestCaseResult(
            description="sort by property crime ascending", dataframe=sorted_df
        )
    )

    # crime totals by state ordered by crime count
    grouped = orig_df.groupBy("state_abbr")
    aliased_col = F.sum("violent_crime").alias("total_crimes")
    ordered_group = grouped.agg(aliased_col).sort(
        col_name="total_crimes", ascending=False
    )
    ret.append(
        TestCaseResult(
            description="crime totals by state ordered by crime count",
            dataframe=ordered_group,
        )
    )

    # sort by property crime ascending on limited df
    limited_df = orig_df.limit(210, 215)
    sorted_df = limited_df.sort("property_crime", ascending=True)
    ret.append(
        TestCaseResult(
            description="sort by property crime ascending on limited df",
            dataframe=sorted_df,
        )
    )

    return ret
