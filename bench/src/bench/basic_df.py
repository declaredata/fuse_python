from declaredata_fuse.dataframe import DataFrame


def simple(df: DataFrame) -> DataFrame:
    return df.limit(0, 1000)
