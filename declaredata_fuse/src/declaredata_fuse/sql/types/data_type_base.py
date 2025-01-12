from abc import ABC, abstractmethod


class DataType(ABC):
    @abstractmethod
    def typeName(self) -> str: ...
    """Get a string representing the name of this type"""
