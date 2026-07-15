from uuid import uuid4

import pytest

from app.domain.entities.review_job import ReviewJob
from app.domain.enums.review_job_status import ReviewJobStatus


@pytest.fixture
def review_job():
    return ReviewJob(
        id=uuid4(),
        pull_request_id=uuid4(),
        status=ReviewJobStatus.PENDING,
    )


def test_start(review_job):
    review_job.start()
    assert review_job.status == ReviewJobStatus.RUNNING
    assert review_job.started_at is not None


def test_complete(review_job):
    review_job.start()
    review_job.complete()
    assert review_job.status == ReviewJobStatus.COMPLETED
    assert review_job.completed_at is not None


def test_fail(review_job):
    review_job.start()
    review_job.fail("Semgrep failed")
    assert review_job.status == ReviewJobStatus.FAILED
    assert review_job.error_message == "Semgrep failed"


def test_cancel(review_job):
    review_job.cancel()
    assert review_job.status == ReviewJobStatus.CANCELLED


def test_invalid_complete(review_job):
    with pytest.raises(ValueError):
        review_job.complete()


def test_invalid_fail(review_job):
    with pytest.raises(ValueError):
        review_job.fail("Error")