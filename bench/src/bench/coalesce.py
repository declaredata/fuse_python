from declaredata_fuse.dataframe import DataFrame
import declaredata_fuse.functions as F


def coalesce_basic(df: DataFrame) -> DataFrame:
    df2 = df.select(
        df.year,
        F.coalesce(df.state_abbr, df.state_name),
    )
    return df2
