from enum import Enum


class FindingSeverity(str, Enum):
    """Severity level of a finding."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"