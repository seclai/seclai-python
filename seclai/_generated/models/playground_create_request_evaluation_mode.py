from enum import Enum


class PlaygroundCreateRequestEvaluationMode(str, Enum):
    MANUAL = "manual"
    PROMPT = "prompt"

    def __str__(self) -> str:
        return str(self.value)
