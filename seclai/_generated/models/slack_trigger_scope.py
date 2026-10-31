from enum import Enum


class SlackTriggerScope(str, Enum):
    BOT_CHANNELS = "bot_channels"
    SELECTED_CHANNELS = "selected_channels"

    def __str__(self) -> str:
        return str(self.value)
