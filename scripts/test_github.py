import asyncio

from app.infrastructure.github.github_service import (
    GitHubAPIService,
)


async def main():

    github = GitHubAPIService()

    pr = await github.get_pull_request(
        "microsoft",
        "vscode",
        1,
    )

    print(pr["title"])


asyncio.run(main())