from enum import Enum


class ServiceUnavailableErrorErrorCode(str, Enum):
    DATABASE_UNAVAILABLE = "database_unavailable"
    VECTOR_STORE_UNAVAILABLE = "vector_store_unavailable"

    def __str__(self) -> str:
        return str(self.value)
