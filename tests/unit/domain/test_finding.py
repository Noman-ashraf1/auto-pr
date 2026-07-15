from uuid import uuid4

import pytest

from app.domain.entities.finding import Finding
from app.domain.enums.finding_category import FindingCategory
from app.domain.enums.finding_severity import FindingSeverity


@pytest.fixture
def finding():
    return Finding(
        id=uuid4(),
        review_job_id=uuid4(),
        title="Hardcoded Secret",
        description="AWS key found",
        severity=FindingSeverity.CRITICAL,
        category=FindingCategory.SECURITY,
        file_path="app/main.py",
        line_number=18,
        rule="G101",
        recommendation="Use environment variables.",
    )


def test_create_finding(finding):
    assert finding.title == "Hardcoded Secret"
    assert finding.severity == FindingSeverity.CRITICAL


def test_empty_title():
    with pytest.raises(ValueError):
        Finding(
            id=uuid4(),
            review_job_id=uuid4(),
            title="",
            description="Test",
            severity=FindingSeverity.LOW,
            category=FindingCategory.CODE_QUALITY,
            file_path="test.py",
            line_number=10,
        )


def test_invalid_line():
    with pytest.raises(ValueError):
        Finding(
            id=uuid4(),
            review_job_id=uuid4(),
            title="Issue",
            description="Test",
            severity=FindingSeverity.LOW,
            category=FindingCategory.STYLE,
            file_path="test.py",
            line_number=0,
        )