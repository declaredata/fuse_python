from fuse_python.dataframe import DataFrame
import fuse_python.functions as F
from fuse_python.window import Window


def window_total_violent_crimes(df: DataFrame) -> DataFrame:
    window_spec = Window.orderBy("violent_crime").rowsBetween(
        Window.unboundedPreceding, 2
    )
    return df.withColumn(
        "running_total_violent_crime", F.sum("violent_crime").over(window_spec)
    )


def window_crimes_per_state(df: DataFrame) -> DataFrame:
    window_spec = Window.orderBy("state_abbr").rowsBetween(
        Window.unboundedPreceding,
        10,
    )
    return df.withColumn("running_total_state_abbr", F.sum("year").over(window_spec))
