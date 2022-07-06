from pydoppler.core import HTTP
from pydoppler.core.endpoint import Endpoints


class Doppler(HTTP):
    def __init__(self, token: str):
        super().__init__(token)

    def fetch_project_list(self, page: int = 1, per_page: int = 20):
        """fetch doppler project list

        :param page: page number
        :param per_page: items per page
        :return: project list
        """
        res = self.get(
            endpoint=Endpoints.projects(),
            params={
                "page": page,
                "per_page": per_page,
            }
        )
        return res

