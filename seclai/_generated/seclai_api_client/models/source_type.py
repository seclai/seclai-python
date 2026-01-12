from enum import Enum


class SourceType(str, Enum):
    CUSTOM_INDEX = "custom_index"
    FILE_UPLOADS = "file_uploads"
    INVALID = "invalid"
    RSS_FEED = "rss_feed"
    WEBSITE = "website"

    def __str__(self) -> str:
        return str(self.value)
