from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.domain.enums.review_job_status import ReviewJobStatus


@dataclass(slots=True)
class ReviewJob:
    """
    Represents one AI review execution.
    """

    id: UUID
    pull_request_id: UUID
    status: ReviewJobStatus
    started_at: datetime | None = None
    completed_at: datetime | None = None
    error_message: str | None = None

    def start(self) -> None:
        if self.status != ReviewJobStatus.PENDING:
            raise ValueError("Only pending jobs can start.")

        self.status = ReviewJobStatus.RUNNING
        self.started_at = datetime.utcnow()

    def complete(self) -> None:
        if self.status != ReviewJobStatus.RUNNING:
            raise ValueError("Only running jobs can complete.")

        self.status = ReviewJobStatus.COMPLETED
        self.completed_at = datetime.utcnow()

    def fail(self, message: str) -> None:
        if self.status != ReviewJobStatus.RUNNING:
            raise ValueError("Only running jobs can fail.")

        self.status = ReviewJobStatus.FAILED
        self.error_message = message
        self.completed_at = datetime.utcnow()

    def cancel(self) -> None:
        if self.status == ReviewJobStatus.COMPLETED:
            raise ValueError("Completed jobs cannot be cancelled.")

        self.status = ReviewJobStatus.CANCELLED
        self.completed_at = datetime.utcnow()