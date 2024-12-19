from unittest.mock import patch
from declaredata_fuse.dataframe import DataFrame


def test_dataframe_col_getattr():
    with patch("declaredata_fuse.proto.sds_pb2_grpc.sdsStub") as stub_mock:
        df = DataFrame(df_uid="1234", stub=stub_mock)
        col11 = df.col1
        col12 = df["col1"]
        assert col11 == col12
