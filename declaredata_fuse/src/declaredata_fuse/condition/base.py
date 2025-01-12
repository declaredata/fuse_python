from abc import ABC, abstractmethod


class BaseCondition(ABC):
    @abstractmethod
    def description(self) -> str: ...

    """
    Get a summary of this condition. Commonly used to create column
    names for `F.when(...)` calls that do not have an alias
    """
