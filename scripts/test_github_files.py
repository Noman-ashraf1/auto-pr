import asyncio

from app.infrastructure.github.github_service import GitHubAPIService


async def main():

    github = GitHubAPIService()

    files = await github.get_pull_request_files(
        owner="Noman-ashraf1",
        repo="auto-pr",
        number=1,  # Change if your PR number is different
    )

    print(f"Found {len(files)} changed files\n")

    for file in files:
        print(f"File: {file.filename}")
        print(f"Status: {file.status}")
        print(f"Changes: +{file.additions} -{file.deletions}")
        print("-" * 50)


asyncio.run(main())