from enum import Enum


class FindingCategory(str, Enum):
    """Type of finding."""

    SECURITY = "security"
    CODE_QUALITY = "code_quality"
    PERFORMANCE = "performance"
    DOCUMENTATION = "documentation"
    STYLE = "style"