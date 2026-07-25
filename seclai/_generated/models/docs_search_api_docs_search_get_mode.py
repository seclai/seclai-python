from enum import Enum


class DocsSearchApiDocsSearchGetMode(str, Enum):
    KEYWORD = "keyword"
    SEMANTIC = "semantic"

    def __str__(self) -> str:
        return str(self.value)
