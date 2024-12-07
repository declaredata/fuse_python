from declaredata_fuse.dataframe import DataFrame
import declaredata_fuse.functions as F


def agg_homicides_per_state(df: DataFrame) -> DataFrame:
    grouped = df.groupBy("state_abbr")
    aliased_col = F.count("homicide").alias("total_homicides")
    return grouped.agg(aliased_col)


def agg_total_crimes_per_year(df: DataFrame) -> DataFrame:
    """number of crimes per year"""
    grouped = df.groupBy("year")
    aliased_col = F.count("year").alias("total_num_crimes")
    return grouped.agg(aliased_col)


def agg_first(df: DataFrame) -> DataFrame:
    grouped = df.groupBy("year")
    return grouped.agg(F.first("population").alias("highest_population_of_year"))


def agg_last(df: DataFrame) -> DataFrame:
    grouped = df.groupBy("year")
    return grouped.agg(F.first("population").alias("lowest_population_of_year"))
