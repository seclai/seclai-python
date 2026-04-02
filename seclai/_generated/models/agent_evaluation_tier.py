from enum import Enum


class AgentEvaluationTier(str, Enum):
    BALANCED = "balanced"
    FAST = "fast"
    THOROUGH = "thorough"

    def __str__(self) -> str:
        return str(self.value)
