from declaredata_fuse.dataframe import DataFrame


def joins_basic(df1: DataFrame) -> DataFrame:
    df2 = df1.filter(df1.year > 1960)
    # the results of the join will be 2x the size of a standard DataFrame
    # from this data source, so just get the first 100 rows so we don't
    # blow up memory
    return df1.join(other=df2, on="year", how="inner").limit(0, 100)
