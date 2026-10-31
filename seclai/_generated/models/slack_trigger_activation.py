from enum import Enum


class SlackTriggerActivation(str, Enum):
    CHANNEL_OPT_IN = "channel_opt_in"
    EVERYWHERE = "everywhere"

    def __str__(self) -> str:
        return str(self.value)
