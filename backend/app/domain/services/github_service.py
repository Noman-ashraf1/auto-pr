from __future__ import annotations

from abc import ABC, abstractmethod


class GitHubService(ABC):
    """
    Interface for interacting with GitHub.
    """

    @abstractmethod
    async def get_pull_request(
        self,
        owner: str,
        repo: str,
        number: int,
    ) -> dict:
        ...