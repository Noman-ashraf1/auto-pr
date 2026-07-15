from enum import Enum


class PullRequestStatus(str, Enum):
    """Represents the lifecycle of a pull request."""

    OPEN = "open"
    UNDER_REVIEW = "under_review"
    APPROVED = "approved"
    CHANGES_REQUESTED = "changes_requested"
    MERGED = "merged"
    CLOSED = "closed"