from datetime import datetime
from uuid import uuid4

import pytest

from app.domain.entities.repository import Repository


@pytest.fixture
def repository() -> Repository:
    return Repository(
        id=uuid4(),
        owner="NomanAshraf",
        name="auto-pr",
        default_branch="main",
        language="Python",
        clone_url="https://github.com/NomanAshraf/auto-pr.git",
        is_private=False,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )


def test_full_name(repository: Repository):
    assert repository.full_name == "NomanAshraf/auto-pr"


def test_is_language(repository: Repository):
    assert repository.is_language("Python")
    assert repository.is_language("python")
    assert not repository.is_language("Go")


def test_rename(repository: Repository):
    repository.rename("guardian-ai")

    assert repository.name == "guardian-ai"


def test_make_private(repository: Repository):
    repository.make_private()

    assert repository.is_private is True


def test_make_public(repository: Repository):
    repository.make_private()
    repository.make_public()

    assert repository.is_private is False


def test_change_default_branch(repository: Repository):
    repository.change_default_branch("develop")

    assert repository.default_branch == "develop"


def test_empty_name_should_fail(repository: Repository):
    with pytest.raises(ValueError):
        repository.rename("")