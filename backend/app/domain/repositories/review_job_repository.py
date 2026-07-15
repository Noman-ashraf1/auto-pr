from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.entities.review_job import ReviewJob


class ReviewJobRepository(ABC):
    """
    Repository interface for ReviewJob.
    """

    @abstractmethod
    def save(self, review_job: ReviewJob) -> None:
        ...

    @abstractmethod
    def get(self, review_job_id: UUID) -> ReviewJob | None:
        ...

    @abstractmethod
    def update(self, review_job: ReviewJob) -> None:
        ...