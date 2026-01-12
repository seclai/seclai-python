from enum import Enum


class ContentFilterType(str, Enum):
    AI_MAIN_CONTENT = "ai_main_content"
    AI_MAIN_CONTENT_SKIP_ADS = "ai_main_content_skip_ads"
    HEADER_FOOTER_NAVIGATION = "header_footer_navigation"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
