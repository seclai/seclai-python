from enum import Enum


class SeedType(str, Enum):
    FULL_HISTORY = "full_history"
    LATEST_N = "latest_n"
    SELECTED_ITEMS = "selected_items"

    def __str__(self) -> str:
        return str(self.value)
