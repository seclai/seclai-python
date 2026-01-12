from enum import Enum


class JsonType(str, Enum):
    ARRAY = "array"
    OBJECT = "object"

    def __str__(self) -> str:
        return str(self.value)
