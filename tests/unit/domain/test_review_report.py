from datetime import datetime
from uuid import uuid4

import pytest

from app.domain.entities.finding import Finding
from app.domain.entities.review_report import ReviewReport
from app.domain.enums.finding_category import FindingCategory
from app.domain.enums.finding_severity import FindingSeverity


@pytest.fixture
def report():
    return ReviewReport(
        id=uuid4(),
        review_job_id=uuid4(),
        created_at=datetime.utcnow(),
    )


def make_finding(job_id):
    return Finding(
        id=uuid4(),
        review_job_id=job_id,
        title="SQL Injection",
        description="Unsanitized query",
        severity=FindingSeverity.CRITICAL,
        category=FindingCategory.SECURITY,
        file_path="db.py",
        line_number=42,
    )


def test_add_finding(report):
    finding = make_finding(report.review_job_id)

    report.add_finding(finding)

    assert report.total_findings == 1


def test_has_critical(report):
    report.add_finding(make_finding(report.review_job_id))

    assert report.has_critical


def test_invalid_job(report):
    with pytest.raises(ValueError):
        report.add_finding(make_finding(uuid4()))