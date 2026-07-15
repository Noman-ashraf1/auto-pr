from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

from app.domain.entities.finding import Finding


@dataclass(slots=True)
class ReviewReport:
    """
    Aggregates all findings for a review job.
    """

    id: UUID
    review_job_id: UUID
    created_at: datetime
    findings: list[Finding] = field(default_factory=list)

    def add_finding(self, finding: Finding) -> None:
        if finding.review_job_id != self.review_job_id:
            raise ValueError(
                "Finding belongs to a different review job."
            )

        self.findings.append(finding)

    @property
    def total_findings(self) -> int:
        return len(self.findings)

    @property
    def has_critical(self) -> bool:
        return any(
            finding.severity.value == "critical"
            for finding in self.findings
        )

    @property
    def has_high(self) -> bool:
        return any(
            finding.severity.value == "high"
            for finding in self.findings
        )