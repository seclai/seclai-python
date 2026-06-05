from enum import Enum


class PendingProcessingCompletedFailedStatus(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed"
    PENDING = "pending"
    PROCESSING = "processing"
    WAITING_HUMAN = "waiting_human"

    def __str__(self) -> str:
        return str(self.value)
