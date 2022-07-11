from pydoppler.core import HTTP
from pydoppler.core.endpoint import Endpoints


class Doppler(HTTP):
    def __init__(self, token: str):
        """Doppler API wrapper

        :param token: doppler api token
        """
        super().__init__(token)

    def retrieve_workspaces(self) -> dict:
        """Retrieve Workspace"""
        res = self._get(endpoint=Endpoints.workspace())
        return res

    def update_workspace(self, name: str, billing_email: str) -> dict:
        """Update Workspace

        :param name: workspace name
        :param billing_email: Billing email
        :return: status json data
        """
        res = self._post(
            endpoint=Endpoints.workspace(),
            json_data={
                "name": name,
                "billing_email": billing_email,
            }
        )
        return res

    def fetch_activity_logs(self, page: int = 1, per_page: int = 20) -> dict:
        res = self._get(
            endpoint=Endpoints.activity_logs(),
            params={
                "page": page,
                "per_page": per_page
            }
        )
        return res

    def retrieve_activity_logs(self, log: str) -> dict:
        """

        :param log: Unique identifier for the log object.
        :return: activity logs
        """

    def fetch_projects(self, page: int = 1, per_page: int = 20) -> dict:
        """fetch doppler project list

        :param page: page number
        :param per_page: items per page
        :return: project list
        """
        res = self._get(
            endpoint=Endpoints.projects(),
            params={
                "page": page,
                "per_page": per_page,
            }
        )
        return res

