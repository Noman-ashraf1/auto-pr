from dataclasses import dataclass


@dataclass(slots=True)
class ReviewRequest:
    repository_owner: str
    repository_name: str
    pull_request_number: int