from enum import Enum


class SpendCapAction(str, Enum):
    DELETE = "delete"
    STOP = "stop"

    def __str__(self) -> str:
        return str(self.value)
