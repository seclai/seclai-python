from enum import Enum


class PendingProcessingCompletedFailedStatus(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed"
    PENDING = "pending"
    PROCESSING = "processing"
    QUEUED = "queued"
    WAITING_HUMAN = "waiting_human"
    WAITING_SCHEDULED = "waiting_scheduled"

    def __str__(self) -> str:
        return str(self.value)
