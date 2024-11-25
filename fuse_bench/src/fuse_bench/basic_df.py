from fuse_python.dataframe import DataFrame


def simple(df: DataFrame) -> DataFrame:
    return df.limit(0, 1000)
