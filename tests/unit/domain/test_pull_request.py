from datetime import datetime
from uuid import uuid4

import pytest

from app.domain.entities.pull_request import PullRequest
from app.domain.enums.pull_request_status import PullRequestStatus


@pytest.fixture
def pull_request() -> PullRequest:
    return PullRequest(
        id=uuid4(),
        repository_id=uuid4(),
        number=1,
        title="Add authentication",
        author="NomanAshraf",
        base_branch="main",
        
        head_branch="feature/auth",
        commit_sha="abc123",
        status=PullRequestStatus.OPEN,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )


def test_start_review(pull_request):
    pull_request.start_review()
    assert pull_request.status == PullRequestStatus.UNDER_REVIEW


def test_approve(pull_request):
    pull_request.start_review()
    pull_request.approve()
    assert pull_request.status == PullRequestStatus.APPROVED


def test_request_changes(pull_request):
    pull_request.start_review()
    pull_request.request_changes()
    assert pull_request.status == PullRequestStatus.CHANGES_REQUESTED


def test_merge(pull_request):
    pull_request.start_review()
    pull_request.approve()
    pull_request.merge()
    assert pull_request.status == PullRequestStatus.MERGED


def test_invalid_merge(pull_request):
    with pytest.raises(ValueError):
        pull_request.merge()


def test_close(pull_request):
    pull_request.close()
    assert pull_request.status == PullRequestStatus.CLOSED