from enum import Enum


class SlackReplyVisibility(str, Enum):
    CHANNEL = "channel"
    PRIVATE = "private"

    def __str__(self) -> str:
        return str(self.value)
