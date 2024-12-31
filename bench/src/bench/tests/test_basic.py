from bench.datasets import get_files
from declaredata_fuse.functions import lit
from pytest_benchmark.fixture import BenchmarkFixture
from bench.tests.setup import setup_dataframe
from declaredata_fuse.row import Row

FILE = get_files()[0]


def test_simple_dataframe(benchmark: BenchmarkFixture):
    def simple() -> list[Row]:
        with setup_dataframe(test_name="simple", file_name=FILE) as df:
            return df.limit(0, 1000).collect()

    result = benchmark(simple)
    assert len(result) == 1000


def test_with_lit(benchmark: BenchmarkFixture) -> None:
    def with_lit() -> list[Row]:
        with setup_dataframe(test_name="with_lit", file_name=FILE) as df:
            return df.select(lit("1").alias("one"), df.year).limit(0, 1000).collect()

    result = benchmark(with_lit)
    assert len(result) == 1000
    for row in result:
        assert isinstance(row, Row)
        row_dict = row.asDict()
        keys = row_dict.keys()
        assert "year" in keys
        assert "one" in keys
