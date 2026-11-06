from enum import Enum


class MetadataKeyWindowResponseWindow(str, Enum):
    ALL_TIME = "all_time"
    LAST_30_DAYS = "last_30_days"
    LAST_7_DAYS = "last_7_days"

    def __str__(self) -> str:
        return str(self.value)
