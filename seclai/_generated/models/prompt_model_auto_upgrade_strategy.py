from enum import Enum


class PromptModelAutoUpgradeStrategy(str, Enum):
    CAUTIOUS_ADOPTER = "cautious_adopter"
    EARLY_ADOPTER = "early_adopter"
    MIDDLE_OF_ROAD = "middle_of_road"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
