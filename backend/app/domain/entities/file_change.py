from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class FileChange:
    """
    Represents a file changed in a pull request.
    """

    filename: str
    status: str
    additions: int
    deletions: int
    changes: int
    patch: str | None

    @property
    def is_python(self) -> bool:
        return self.filename.endswith(".py")

    @property
    def is_deleted(self) -> bool:
        return self.status == "removed"

    @property
    def is_added(self) -> bool:
        return self.status == "added"

    @property
    def is_modified(self) -> bool:
        return self.status == "modified"