from enum import Enum


class PollingAction(str, Enum):
    NEW = "new"
    NEW_AND_UPDATED = "new_and_updated"

    def __str__(self) -> str:
        return str(self.value)
