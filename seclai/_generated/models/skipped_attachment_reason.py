from enum import Enum


class SkippedAttachmentReason(str, Enum):
    DISPLAYED_IN_BODY = "displayed_in_body"
    NO_FILENAME = "no_filename"
    OVER_CAP = "over_cap"
    UNDECODABLE = "undecodable"

    def __str__(self) -> str:
        return str(self.value)
