from typing import TypedDict


class ApiException(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


class PostJson(TypedDict):
    creator: str
    content: str
    likes: int
    datetime: str
    comments: list[str] | None
