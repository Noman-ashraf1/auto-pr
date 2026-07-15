from uuid import UUID

from app.domain.entities.review_job import ReviewJob
from app.domain.repositories.review_job_repository import (
    ReviewJobRepository,
)


class InMemoryReviewJobRepository(ReviewJobRepository):
    """
    Repository used for unit tests.
    """

    def __init__(self):
        self._storage: dict[UUID, ReviewJob] = {}

    def save(self, review_job: ReviewJob) -> None:
        self._storage[review_job.id] = review_job

    def get(self, review_job_id: UUID) -> ReviewJob | None:
        return self._storage.get(review_job_id)

    def update(self, review_job: ReviewJob) -> None:
        self._storage[review_job.id] = review_job