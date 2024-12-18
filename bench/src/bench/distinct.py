from declaredata_fuse.dataframe import DataFrame


def distinct_basic(df: DataFrame) -> DataFrame:
    return df.distinct()
