from enum import Enum


class SpendCapDeleteOrder(str, Enum):
    LARGEST_FIRST = "largest_first"
    OLDEST_ADDED = "oldest_added"
    OLDEST_PUBLISHED = "oldest_published"

    def __str__(self) -> str:
        return str(self.value)
