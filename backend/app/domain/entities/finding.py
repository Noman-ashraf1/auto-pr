from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from app.domain.enums.finding_category import FindingCategory
from app.domain.enums.finding_severity import FindingSeverity


@dataclass(slots=True)
class Finding:
    """
    Represents one issue discovered during a review.
    """

    id: UUID
    review_job_id: UUID

    title: str
    description: str

    severity: FindingSeverity
    category: FindingCategory

    file_path: str
    line_number: int

    rule: str | None = None
    recommendation: str | None = None

    def __post_init__(self) -> None:
        self.title = self.title.strip()

        if not self.title:
            raise ValueError("Title cannot be empty.")

        if self.line_number <= 0:
            raise ValueError("Line number must be greater than zero.")