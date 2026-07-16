from pathlib import Path

from git import Repo


class GitService:
    """
    Handles cloning and checking out Git repositories.
    """

    def clone_repository(
        self,
        repo_url: str,
        destination: Path,
    ) -> Repo:
        """
        Clone a repository to the destination directory.
        """
        return Repo.clone_from(repo_url, destination)

    def checkout_branch(
        self,
        repo: Repo,
        branch: str,
    ) -> None:
        """
        Checkout a branch.
        """
        repo.git.checkout(branch)

    def checkout_commit(
        self,
        repo: Repo,
        commit_sha: str,
    ) -> None:
        """
        Checkout a specific commit.
        """
        repo.git.checkout(commit_sha)