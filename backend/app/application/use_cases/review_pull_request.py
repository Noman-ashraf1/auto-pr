from uuid import uuid4

from app.application.dto.review_request import ReviewRequest
from app.domain.entities.review_job import ReviewJob
from app.domain.enums.review_job_status import ReviewJobStatus
from app.domain.repositories.review_job_repository import (
    ReviewJobRepository,
)


class ReviewPullRequestUseCase:
    """
    Starts a review job.
    """

    def __init__(
        self,
        repository: ReviewJobRepository,
    ):
        self.repository = repository

    def execute(
        self,
        request: ReviewRequest,
    ) -> ReviewJob:

        review_job = ReviewJob(
            id=uuid4(),
            pull_request_id=uuid4(),
            status=ReviewJobStatus.PENDING,
        )

        self.repository.save(review_job)

        return review_job