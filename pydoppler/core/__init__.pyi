from httpx import Client


class HTTP:
    def __init__(self, token: str) -> None: ...
    def session(self) -> Client: ...
    def get(self, endpoint: str, params: dict | None) -> dict: ...
    def post(
        self,
        endpoint: str,
        params: dict | None,
        json_data: dict | None,
        data: dict | None,
    ) -> dict: ...
