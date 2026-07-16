import httpx

from app.domain.entities.file_change import FileChange
from app.domain.services.github_service import GitHubService


class GitHubAPIService(GitHubService):

    BASE_URL = "https://api.github.com"

    async def get_pull_request(
        self,
        owner: str,
        repo: str,
        number: int,
    ) -> dict:

        async with httpx.AsyncClient() as client:

            response = await client.get(
                f"{self.BASE_URL}/repos/{owner}/{repo}/pulls/{number}"
            )

            if response.status_code == 404:
                raise ValueError(
                    f"Pull request {number} not found in {owner}/{repo}"
                )

            response.raise_for_status()

            return response.json()

    async def get_pull_request_files(
        self,
        owner: str,
        repo: str,
        number: int,
    ) -> list[FileChange]:

        async with httpx.AsyncClient() as client:

            response = await client.get(
                f"{self.BASE_URL}/repos/{owner}/{repo}/pulls/{number}/files"
            )

            if response.status_code == 404:
                raise ValueError(
                    f"Pull request {number} not found in {owner}/{repo}"
                )

            response.raise_for_status()

            files = []

            for item in response.json():

                files.append(
                    FileChange(
                        filename=item["filename"],
                        status=item["status"],
                        additions=item["additions"],
                        deletions=item["deletions"],
                        changes=item["changes"],
                        patch=item.get("patch"),
                    )
                )

            return files