from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class Repository:
    """
    Represents a source code repository.

    This is a pure domain entity that contains only
    business data and behavior.

    It has no dependency on:
    - FastAPI
    - SQLAlchemy
    - GitHub API
    - LangGraph
    """

    id: UUID
    owner: str
    name: str
    default_branch: str
    language: str | None
    clone_url: str
    is_private: bool
    created_at: datetime
    updated_at: datetime

    def __post_init__(self) -> None:
        """Validate repository data after initialization."""

        self.owner = self.owner.strip()
        self.name = self.name.strip()
        self.default_branch = self.default_branch.strip()

        if not self.owner:
            raise ValueError("Repository owner cannot be empty.")

        if not self.name:
            raise ValueError("Repository name cannot be empty.")

        if not self.default_branch:
            raise ValueError("Default branch cannot be empty.")

    @property
    def full_name(self) -> str:
        """
        Returns the repository full name.

        Example:
            NomanAshraf/auto-pr
        """
        return f"{self.owner}/{self.name}"

    def is_language(self, language: str) -> bool:
        """
        Check whether the repository uses the given language.

        Example:
            repo.is_language("Python")
        """
        if self.language is None:
            return False

        return self.language.lower() == language.lower()

    def rename(self, new_name: str) -> None:
        """
        Rename the repository.
        """

        new_name = new_name.strip()

        if not new_name:
            raise ValueError("Repository name cannot be empty.")

        self.name = new_name
        self.updated_at = datetime.utcnow()

    def change_default_branch(self, branch: str) -> None:
        """
        Change the default branch.
        """

        branch = branch.strip()

        if not branch:
            raise ValueError("Branch name cannot be empty.")

        self.default_branch = branch
        self.updated_at = datetime.utcnow()

    def make_private(self) -> None:
        """Mark the repository as private."""
        self.is_private = True
        self.updated_at = datetime.utcnow()

    def make_public(self) -> None:
        """Mark the repository as public."""
        self.is_private = False
        self.updated_at = datetime.utcnow()

    def __str__(self) -> str:
        return self.full_name