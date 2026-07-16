from abc import ABC, abstractmethod

from app.domain.entities.file_change import FileChange


class GitHubService(ABC):

    @abstractmethod
    async def get_pull_request(
        self,
        owner: str,
        repo: str,
        number: int,
    ) -> dict:
        ...

    @abstractmethod
    async def get_pull_request_files(
        self,
        owner: str,
        repo: str,
        number: int,
    ) -> list[FileChange]:
        ...