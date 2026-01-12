from enum import Enum


class AgentTriggerType(str, Enum):
    CONTENT_ADDED = "content_added"
    CONTENT_ADDED_OR_UPDATED = "content_added_or_updated"
    CONTENT_UPDATED = "content_updated"
    DYNAMIC_INPUT = "dynamic_input"
    TEMPLATE_INPUT = "template_input"

    def __str__(self) -> str:
        return str(self.value)
