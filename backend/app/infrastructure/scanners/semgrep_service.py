from __future__ import annotations

import json
import subprocess
from pathlib import Path
from uuid import uuid4

from app.domain.entities.finding import Finding
from app.domain.enums.finding_category import FindingCategory
from app.domain.enums.finding_severity import FindingSeverity


class SemgrepService:
    """
    Runs Semgrep and converts the output into domain Finding entities.
    """

    def scan(self, repository: Path) -> list[Finding]:

        result = subprocess.run(
            [
                "semgrep",
                "--config",
                "auto",
                "--json",
                str(repository),
            ],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            raise RuntimeError(result.stderr)

        data = json.loads(result.stdout)

        findings: list[Finding] = []

        for item in data["results"]:

            findings.append(
                Finding(
                    id=uuid4(),
                    review_job_id=uuid4(),
                    title=item["check_id"],
                    description=item["extra"]["message"],
                    severity=self._map_severity(item),
                    category=self._map_category(item),
                    file_path=item["path"],
                    line_number=item["start"]["line"],
                    rule=item["check_id"],
                    recommendation=item["extra"].get("fix"),
                )
            )

        return findings

    def _map_severity(
        self,
        finding: dict,
    ) -> FindingSeverity:

        severity = (
            finding.get("extra", {})
            .get("severity", "INFO")
            .upper()
        )

        mapping = {
            "ERROR": FindingSeverity.CRITICAL,
            "WARNING": FindingSeverity.HIGH,
            "INFO": FindingSeverity.LOW,
        }

        return mapping.get(severity, FindingSeverity.MEDIUM)

    def _map_category(
        self,
        finding: dict,
    ) -> FindingCategory:

        rule = finding["check_id"].lower()

        if "security" in rule:
            return FindingCategory.SECURITY

        if "performance" in rule:
            return FindingCategory.PERFORMANCE

        if "style" in rule:
            return FindingCategory.STYLE

        if "doc" in rule:
            return FindingCategory.DOCUMENTATION

        return FindingCategory.CODE_QUALITY