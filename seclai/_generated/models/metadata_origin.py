from enum import Enum


class MetadataOrigin(str, Enum):
    CUSTOM = "custom"
    SOURCE = "source"
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)
