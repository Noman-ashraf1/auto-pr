from enum import Enum


class ReviewJobStatus(str, Enum):
    """Lifecycle of a review job."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"