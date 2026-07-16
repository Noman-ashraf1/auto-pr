from pathlib import Path
import shutil

from app.infrastructure.github.github_service import GitHubAPIService
from app.infrastructure.git.git_service import GitService
from app.infrastructure.scanners.semgrep_service import SemgrepService
from app.infrastructure.scanners.bandit_service import BanditService


class ReviewPipeline:
    """
    Coordinates the complete pull request review workflow.
    """

    def __init__(self):
        self.github = GitHubAPIService()
        self.git = GitService()

        self.semgrep = SemgrepService()
        self.bandit = BanditService()

    async def run(
        self,
        owner: str,
        repo: str,
        number: int,
        destination: Path = Path("tmp_repo"),
    ):
        # Clean any previous clone
        if destination.exists():
            shutil.rmtree(destination)

        # --------------------------------------------------
        # Step 1: Fetch the pull request details
        # --------------------------------------------------
        pr = await self.github.get_pull_request(
            owner=owner,
            repo=repo,
            number=number,
        )

        print(f"Pull Request: {pr['title']}")

        # --------------------------------------------------
        # Step 2: Fetch changed files
        # --------------------------------------------------
        changed_files = await self.github.get_pull_request_files(
            owner=owner,
            repo=repo,
            number=number,
        )

        print(f"Changed Files: {len(changed_files)}")

        # --------------------------------------------------
        # Step 3: Clone repository
        # --------------------------------------------------
        repository = self.git.clone_repository(
            repo_url=f"https://github.com/{owner}/{repo}.git",
            destination=destination,
        )

        print("Repository cloned successfully.")

        # --------------------------------------------------
        # Step 4: Checkout the PR branch
        # --------------------------------------------------
        self.git.checkout_branch(
            repository,
            pr["head"]["ref"],
        )

        print(f"Checked out branch: {pr['head']['ref']}")

        # --------------------------------------------------
        # Step 5: Run Semgrep
        # --------------------------------------------------
        semgrep_findings = self.semgrep.scan(destination)

        print(f"Semgrep Findings: {len(semgrep_findings)}")

        # --------------------------------------------------
        # Step 6: Run Bandit
        # --------------------------------------------------
        bandit_findings = self.bandit.scan(destination)

        print(f"Bandit Findings: {len(bandit_findings)}")

        # --------------------------------------------------
        # Step 7: Merge findings
        # --------------------------------------------------
        findings = []

        findings.extend(semgrep_findings)
        findings.extend(bandit_findings)

        print(f"Total Findings: {len(findings)}")

        return findings
