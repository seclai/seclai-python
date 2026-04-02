from enum import Enum


class EvaluationStatus(str, Enum):
    ERROR = "error"
    FAILED = "failed"
    PASSED = "passed"
    PENDING = "pending"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)
