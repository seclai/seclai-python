from enum import Enum


class SourceIndexMode(str, Enum):
    BALANCED = "balanced"
    CUSTOM = "custom"
    FAST_AND_CHEAP = "fast_and_cheap"
    SLOW_AND_THOROUGH = "slow_and_thorough"

    def __str__(self) -> str:
        return str(self.value)
