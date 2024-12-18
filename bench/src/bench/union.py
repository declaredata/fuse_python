from declaredata_fuse.dataframe import DataFrame


def union_basic(df: DataFrame) -> DataFrame:
    df2 = df.filter(df.year > 1900)
    # we're gonna have 2x the amount of data in this DataFrame, so
    # limit its output to avoid blowing up
    return df.union(other=df2).limit(0, 100)
