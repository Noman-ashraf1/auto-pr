from __future__ import annotations

import json
import subprocess
from pathlib import Path
from uuid import uuid4

from app.domain.entities.finding import Finding
from app.domain.enums.finding_category import FindingCategory
from app.domain.enums.finding_severity import FindingSeverity


class BanditService:
    """
    Runs Bandit against a repository and converts the results
    into domain Finding entities.
    """

    def scan(self, repository: Path) -> list[Finding]:

        result = subprocess.run(
            [
                "bandit",
                "-r",
                str(repository),
                "-x",                      # Exclude test files
                f"{repository}/tests",
                "-f",
                "json",
            ],
            capture_output=True,
            text=True,
        )

        if result.returncode not in (0, 1):
            raise RuntimeError(
                f"Bandit failed:\n{result.stderr}"
            )

        data = json.loads(result.stdout)

        findings: list[Finding] = []

        for item in data.get("results", []):

            findings.append(
                Finding(
                    id=uuid4(),
                    review_job_id=uuid4(),
                    title=item["test_name"],
                    description=item["issue_text"],
                    severity=self._map_severity(
                        item["issue_severity"]
                    ),
                    category=FindingCategory.SECURITY,
                    file_path=item["filename"],
                    line_number=item["line_number"],
                    rule=item["test_id"],
                    recommendation=item.get("more_info"),
                )
            )

        return findings

    @staticmethod
    def _map_severity(
        severity: str,
    ) -> FindingSeverity:

        mapping = {
            "LOW": FindingSeverity.LOW,
            "MEDIUM": FindingSeverity.MEDIUM,
            "HIGH": FindingSeverity.HIGH,
        }

        return mapping.get(
            severity.upper(),
            FindingSeverity.LOW,
        )