from enum import Enum


class MembershipType(str, Enum):
    ADMINISTRATOR = "administrator"
    OWNER = "owner"
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
