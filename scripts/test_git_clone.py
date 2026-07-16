from pathlib import Path
import shutil

from app.infrastructure.git.git_service import GitService


destination = Path("tmp_repo")

if destination.exists():
    shutil.rmtree(destination)

git_service = GitService()

repo = git_service.clone_repository(
    repo_url="https://github.com/Noman-ashraf1/auto-pr.git",
    destination=destination,
)

print("Repository cloned successfully!")
print("Current branch:", repo.active_branch.name)