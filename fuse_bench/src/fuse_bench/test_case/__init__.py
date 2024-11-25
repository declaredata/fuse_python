from dataclasses import dataclass

from fuse_python.dataframe import DataFrame


@dataclass(frozen=True)
class TestCaseResult:
    description: str
    dataframe: DataFrame
