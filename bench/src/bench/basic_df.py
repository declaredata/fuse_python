from declaredata_fuse.dataframe import DataFrame
from declaredata_fuse.functions import lit


def simple(df: DataFrame) -> DataFrame:
    return df.limit(0, 1000)

def with_lit(df: DataFrame) -> DataFrame:
    return df.select(lit("1").alias("one"), df.year).limit(0, 1000)
