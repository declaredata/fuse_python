from fuse_python.dataframe import DataFrame


def select(df: DataFrame) -> DataFrame:
    return df.select(
        df.year,
        df.state_abbr,
        (df.violent_crime + 1).alias(new_name="violent_crime_div_100"),
    )
