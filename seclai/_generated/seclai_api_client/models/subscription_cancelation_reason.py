from enum import Enum


class SubscriptionCancelationReason(str, Enum):
    CONTENT_SOURCE_TYPE_NOT_SUPPORTED = "content_source_type_not_supported"
    FOUND_BETTER_SERVICE = "found_better_service"
    NOT_USING_ENOUGH = "not_using_enough"
    OTHER = "other"
    TECHNICAL_ISSUES = "technical_issues"
    TEMPORARY_NEED = "temporary_need"
    TOO_EXPENSIVE = "too_expensive"
    USE_CASE_NOT_SUPPORTED = "use_case_not_supported"
    WEBSITE_DOES_NOT_ALLOW_SCRAPING = "website_does_not_allow_scraping"

    def __str__(self) -> str:
        return str(self.value)
