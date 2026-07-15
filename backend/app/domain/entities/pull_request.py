from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.domain.enums.pull_request_status import PullRequestStatus


@dataclass(slots=True)
class PullRequest:
    """
    Represents a Git pull request.

    Pure domain entity.
    """

    id: UUID
    repository_id: UUID
    number: int
    title: str
    author: str
    base_branch: str
    head_branch: str
    commit_sha: str
    status: PullRequestStatus
    created_at: datetime
    updated_at: datetime

    def __post_init__(self) -> None:
        self.title = self.title.strip()

        if not self.title:
            raise ValueError("Title cannot be empty.")

        if self.number <= 0:
            raise ValueError("Pull request number must be greater than zero.")

    def start_review(self) -> None:
        if self.status != PullRequestStatus.OPEN:
            raise ValueError("Only open pull requests can start review.")

        self.status = PullRequestStatus.UNDER_REVIEW
        self.updated_at = datetime.utcnow()

    def approve(self) -> None:
        if self.status != PullRequestStatus.UNDER_REVIEW:
            raise ValueError("Pull request must be under review.")

        self.status = PullRequestStatus.APPROVED
        self.updated_at = datetime.utcnow()

    def request_changes(self) -> None:
        if self.status != PullRequestStatus.UNDER_REVIEW:
            raise ValueError("Pull request must be under review.")

        self.status = PullRequestStatus.CHANGES_REQUESTED
        self.updated_at = datetime.utcnow()

    def merge(self) -> None:
        if self.status != PullRequestStatus.APPROVED:
            raise ValueError("Only approved pull requests can be merged.")

        self.status = PullRequestStatus.MERGED
        self.updated_at = datetime.utcnow()

    def close(self) -> None:
        if self.status == PullRequestStatus.MERGED:
            raise ValueError("Merged pull requests cannot be closed.")

        self.status = PullRequestStatus.CLOSED
        self.updated_at = datetime.utcnow()