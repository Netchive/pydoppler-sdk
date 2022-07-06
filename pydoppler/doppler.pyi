from pydoppler.core import HTTP


class Doppler(HTTP):
    def __init__(self, token: str) -> None:...

    def fetch_project_list(self, page: int = 1, per_page: int = 20) -> dict:...