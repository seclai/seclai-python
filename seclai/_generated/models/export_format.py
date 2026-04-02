from enum import Enum


class ExportFormat(str, Enum):
    CSV = "csv"
    JSONL = "jsonl"
    PARQUET = "parquet"
    ZIP = "zip"

    def __str__(self) -> str:
        return str(self.value)
