from pathlib import Path

from app.infrastructure.scanners.semgrep_service import SemgrepService

scanner = SemgrepService()

findings = scanner.scan(Path("tmp_repo"))

print(f"\nFound {len(findings)} findings\n")

for finding in findings:

    print("=" * 60)
    print("Title:", finding.title)
    print("Severity:", finding.severity.value)
    print("Category:", finding.category.value)
    print("File:", finding.file_path)
    print("Line:", finding.line_number)
    print("Description:", finding.description)