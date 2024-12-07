from bench.agg import (
    agg_first,
    agg_homicides_per_state,
    agg_last,
    agg_total_crimes_per_year,
)
from bench.drop import drop
from bench.selects import select
from bench.basic_df import simple
from bench.test_case.runner import TestCase
from bench.window import window_crimes_per_state, window_total_violent_crimes


def get_test_cases(file: str, verbose: bool) -> list[TestCase]:
    return [
        TestCase(
            test_name="DataFrame.simple",
            file_name=file,
            runner=simple,
            verbose=verbose,
        ),
        TestCase(
            test_name="DataFrame.select",
            file_name=file,
            runner=select,
            verbose=verbose,
        ),
        TestCase(
            test_name="DataFrame.drop",
            file_name=file,
            runner=drop,
            verbose=verbose,
        ),
        TestCase(
            test_name="DataFrame.aggregation.homicides_per_state",
            file_name=file,
            runner=agg_homicides_per_state,
            verbose=verbose,
        ),
        TestCase(
            test_name="DataFrame.aggregation.total_crimes_per_year",
            file_name=file,
            runner=agg_total_crimes_per_year,
            verbose=verbose,
        ),
        TestCase(
            test_name="DataFrame.aggregation.first",
            file_name=file,
            runner=agg_first,
            verbose=verbose,
        ),
        TestCase(
            test_name="DataFrame.aggregation.lsat",
            file_name=file,
            runner=agg_last,
            verbose=verbose,
        ),
        TestCase(
            test_name="DataFrame.windowing.total_violent_crimes",
            file_name=file,
            runner=window_total_violent_crimes,
            verbose=verbose,
        ),
        TestCase(
            test_name="DataFrame.aggregation.crimes_per_state",
            file_name=file,
            runner=window_crimes_per_state,
            verbose=verbose,
        ),
    ]
