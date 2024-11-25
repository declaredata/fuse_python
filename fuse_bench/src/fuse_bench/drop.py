from fuse_python.dataframe import DataFrame


def drop(orig_df: DataFrame) -> DataFrame:
    return orig_df.drop("state_name", orig_df.caveats).limit(0, 1000)
