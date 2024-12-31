from bench.datasets import get_files
from bench.tests.setup import setup_dataframe
from declaredata_fuse.row import Row
from pytest_benchmark.fixture import BenchmarkFixture
import declaredata_fuse.functions as F

def test_agg_simple(benchmark: BenchmarkFixture) -> None:
    def run() -> list[Row]:
        with setup_dataframe(
            test_name="agg_simple",
            file_name=get_files()[0],
        ) as df:
            grouped = df.groupBy("state_abbr")
            aliased_col = F.count("homicide").alias("total_homicides")
            return grouped.agg(aliased_col).collect()
    result = benchmark(run)
    # there should be 52, not 50 results, because we have all 50 states plus
    # the following:
    # 
    # * an empty value (used to indicate all of the US)
    # * Washington D.C. ('DC')
    assert len(result) == 52
