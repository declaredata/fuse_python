from bench.datasets import get_files
from bench.tests.setup import setup_dataframe

FILE = get_files()[0]


def test_alias_dataframe():
    with setup_dataframe(test_name="simple", file_name=FILE) as df:
        df_aliased = df.alias("mynewdf")
        rows = df_aliased.collect()
        assert len(rows) > 0
        row = rows[0]
        all_cols = [key for key in row.asDict().keys()]
        for col in all_cols:
            assert col.startswith("mynewdf")
