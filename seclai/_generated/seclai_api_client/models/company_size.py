from enum import Enum


class CompanySize(str, Enum):
    JUST_ME = "just_me"
    SIZE_11_50 = "size_11_50"
    SIZE_2_10 = "size_2_10"
    SIZE_51_PLUS = "size_51_plus"

    def __str__(self) -> str:
        return str(self.value)
