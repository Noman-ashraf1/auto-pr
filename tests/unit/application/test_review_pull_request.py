from app.application.dto.review_request import ReviewRequest
from app.application.use_cases.review_pull_request import (
    ReviewPullRequestUseCase,
)
from app.infrastructure.persistence.in_memory_review_job_repository import (
    InMemoryReviewJobRepository,
)
from app.domain.enums.review_job_status import ReviewJobStatus


def test_execute():

    repo = InMemoryReviewJobRepository()

    use_case = ReviewPullRequestUseCase(repo)

    request = ReviewRequest(
        repository_owner="NomanAshraf",
        repository_name="auto-pr",
        pull_request_number=1,
    )

    review_job = use_case.execute(request)

    assert review_job.status == ReviewJobStatus.PENDING

    assert repo.get(review_job.id) is not None