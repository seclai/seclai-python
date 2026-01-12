from enum import Enum


class PollingType(str, Enum):
    DAILY = "daily"
    HOURLY = "hourly"
    MANUALLY = "manually"
    ONCE = "once"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
