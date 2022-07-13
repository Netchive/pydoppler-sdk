from _typeshed import Self

class PydopplerError(Exception):
    def __init__(self: Self, message: str, status_code: int) -> None:...
    def __str__(self: Self) -> str:...


class HTTP:
    def __init__(self: Self, token: str) -> None: ...
    def _get(
        self: Self,
        endpoint: str,
        params: dict | None = ...
    ) -> dict: ...
    def _post(
        self: Self,
        endpoint: str,
        params: dict | None = ...,
        json_data: dict | None = ...,
        data: dict | None = ...,
    ) -> dict: ...
    def _delete(
        self: Self,
        endpoint: str,
        params: dict | None = ...,
    ) -> dict:...
    def _put(
        self: Self,
        endpoint: str,
        params: dict | None = ...,
        json_data: dict | None = ...,
        data: dict | None = ...,
    ) -> dict: ...

