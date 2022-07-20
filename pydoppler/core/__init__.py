from httpx import Client
from pydoppler.auth import basic_auth_header_value
from pydoppler.auth import check_token
from pydoppler.core.endpoint import Endpoints


class PydopplerError(Exception):
    def __init__(self, message, status_code) -> None:
        self.message = message
        self.status_code = status_code
        super().__init__(message)

    def __str__(self) -> str:
        return f"{self.status_code} -> {self.message}"


class HTTP:
    def __init__(self, token: str):
        self._basic_auth = basic_auth_header_value(doppler_token=check_token(token))

    def _get(
        self,
        endpoint: str,
        params: dict | None = None,
        headers: dict | None = None
    ) -> dict:
        """HTTP GET Method

        :param endpoint: doppler api url
        :param params: request params dictionary
        :param headers: request headers dictionary
        :return: http response json object
        """
        with Client(headers={"Authorization": self._basic_auth}) as client:
            response = client.get(url=endpoint, params=params, headers=headers)
            if not response.is_success:
                if not response.is_server_error:
                    if response.json().get("messages"):
                        raise PydopplerError(
                            status_code=response.status_code,
                            message=response.json()["messages"],
                        )
                    else:
                        raise PydopplerError(
                            status_code=response.status_code,
                            message=str(response.json())
                        )
                else:
                    raise PydopplerError(
                        status_code=response.status_code,
                        message="Doppler API Server Error",
                    )
            else:
                return response.json()

    def _post(
        self,
        endpoint: str,
        params: dict | None = None,
        json_data: dict | None = None,
        data: dict | None = None,
        headers: dict | None = None
    ) -> dict:
        """HTTP POST Method

        :param endpoint: doppler api url
        :param params: request params dictionary
        :param json_data: request json data
        :param data: request body data
        :param headers: request headers dictionary
        :return: response json data
        """
        with Client(headers={"Authorization": self._basic_auth}) as client:
            response = client.post(
                url=endpoint, params=params, json=json_data, data=data, headers=headers
            )
            if not response.is_success:
                if not response.is_server_error:
                    raise PydopplerError(
                        status_code=response.status_code,
                        message=response.json()["message"],
                    )
                else:
                    raise PydopplerError(
                        status_code=response.status_code,
                        message="Doppler API Server Error",
                    )
            else:
                return response.json()

    def _delete(
        self,
        endpoint: str,
        params: dict | None,
        headers: dict | None = None
    ) -> dict:
        """HTTP DELETE Method

        :param endpoint: doppler api url
        :param params: request params dictionary
        :param headers: request headers dictionary
        :return: http response json object
        """

        with Client(headers={"Authorization": self._basic_auth}) as client:
            response = client.delete(url=endpoint, params=params, headers=headers)
            if not response.is_success:
                if not response.is_server_error:
                    raise PydopplerError(
                        status_code=response.status_code,
                        message=response.json()["message"],
                    )
                else:
                    raise PydopplerError(
                        status_code=response.status_code,
                        message="Doppler API Server Error",
                    )
            else:
                return response.json()

    def _put(
        self,
        endpoint: str,
        params: dict | None = None,
        json_data: dict | None = None,
        data: dict | None = None,
        headers: dict | None = None
    ):
        """HTTP PUT Method

        :param endpoint: doppler api url
        :param params: request params dictionary
        :param json_data: request json data
        :param data: request body data
        :param headers: request headers dictionary
        :return: response json data
        """
        with Client(headers={"Authorization": self._basic_auth}) as client:
            response = client.put(
                url=endpoint, params=params, json=json_data, data=data, headers=headers
            )
            if not response.is_success:
                if not response.is_server_error:
                    raise PydopplerError(
                        status_code=response.status_code,
                        message=response.json()["message"],
                    )
                else:
                    raise PydopplerError(
                        status_code=response.status_code,
                        message="Doppler API Server Error",
                    )
            else:
                return response.json()


__all__ = ["PydopplerError", "HTTP", "Endpoints"]
