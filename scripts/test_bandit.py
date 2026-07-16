from pathlib import Path

from app.infrastructure.scanners.bandit_service import BanditService

scanner = BanditService()

findings = scanner.scan(Path("tmp_repo"))

print(f"Found {len(findings)} findings\n")

for finding in findings:
    print(finding.title)
    print(finding.file_path)
    print(finding.severity.value)
    print("-" * 40)