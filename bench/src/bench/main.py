import time
from bench.datasets import get_files
import click

from bench.collect import df_collect
from bench.test_case.printer import print_limited_results
from bench.test_case.runner import run_df_test_case
from bench.test_cases import get_test_cases
from bench.basic_sql import sql_api
from bench.sorts import sorts_api


FILES = get_files()


@click.command()
@click.option(
    "--verbose",
    default=False,
    help="Whether to print dataframe results (True), or just timings (False).",
)
def run(verbose: bool) -> None:
    for file in FILES:
        print(f"\n\n\tFILE: {file}\n\n")
        start_time = time.perf_counter()
        run_single_file(f"file {file}", file, verbose)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"\n\n\ttotal: {elapsed_time}\n\n")


def run_single_file(description: str, file: str, verbose: bool):
    for tc in get_test_cases(file=file, verbose=verbose):
        run_df_test_case(tc=tc)

    print("Starting SQL API Benchmark")
    with sql_api(file) as (df1, elapsed):
        if verbose:
            print(df1.limit(0, 10).pretty_print())
        print(f"[{description}] SQL API test took {elapsed} sec")

    print("Starting DataFrame.collect test")
    with df_collect(file) as (collected_rows, elapsed):
        print(
            f"[{description}] ",
            f"Computing {len(collected_rows)} collected rows took {elapsed} sec",
        )
        if verbose:
            for idx, row in enumerate(collected_rows):
                print(f"{idx}: {row}")

    print("Starting Sort/Filter API benchmark")
    with sorts_api(file) as (filtered_dataframes, elapsed):
        print(
            f"[{description}] ",
            f"Computing {len(filtered_dataframes)} sort/filter operations "
            f"took {elapsed} sec",
        )
        if verbose:
            print_limited_results(filtered_dataframes)


if __name__ == "__main__":
    run()
