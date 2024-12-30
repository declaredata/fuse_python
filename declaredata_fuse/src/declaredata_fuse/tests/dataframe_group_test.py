from unittest.mock import patch
from declaredata_fuse.dataframe import DataFrame
from declaredata_fuse.grouped import Grouped


def test_group_by() -> None:
    with patch("declaredata_fuse.proto.sds_pb2_grpc.sdsStub") as stub_mock:
        df = DataFrame(df_uid="1234", stub=stub_mock)
        COL_NAME = "somecol"
        grouped_single_col = df.groupBy(col_name=COL_NAME)
        multi_cols = [f"{COL_NAME}{i}" for i in range(10)]
        grouped_multi_col = df.groupBy(col_name=multi_cols)

        _assert_grouped(
            grouped=grouped_single_col,
            orig_df=df,
            expected_cols=[COL_NAME],
        )
        _assert_grouped(
            grouped=grouped_multi_col,
            orig_df=df,
            expected_cols=multi_cols,
        )


def _assert_grouped(
    *,
    grouped: Grouped,
    orig_df: DataFrame,
    expected_cols: list[str],
) -> None:
    assert grouped.group_cols == expected_cols
    assert grouped.df_uid == orig_df.df_uid
