from dataclasses import dataclass

from declaredata_fuse.dataframe import DataFrame


@dataclass(frozen=True)
class TestCaseResult:
    description: str
    dataframe: DataFrame
