from fuse_bench.test_case import TestCaseResult


def print_limited_results(results: list[TestCaseResult]) -> None:
    for tcr in results:
        print(f"{tcr.description} (first 10):")
        print(tcr.dataframe.limit(0, 10).pretty_print())
