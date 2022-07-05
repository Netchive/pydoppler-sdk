from httpx import Client
from pydoppler.auth.vaildator import check_token
from pydoppler.auth import basic_auth_header_value


class PydopplerError(Exception):
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

    def __str__(self) -> str:
        return f"{self.status_code} -> {self.message}"


class HTTP:
    def __init__(self, token: str):
        self._basic_auth = basic_auth_header_value(
            doppler_token=check_token(token)
        )

    def sessions(self) -> Client:
        _client = Client(
            headers=self._basic_auth
        )
        return _client

    def get(self, endpoint: str, params: dict | None) -> dict:
        """HTTP GET request

        :param endpoint: doppler api url
        :param params:
        :return:
        """
        session = self.sessions()
        response = session.get(url=endpoint, params=params)
        if not response.is_success:
            if not response.is_server_error:
                raise PydopplerError(
                    status_code=response.status_code,
                    message=response.json()["message"]
                )
            else:
                raise PydopplerError(
                    status_code=response.status_code,
                    message="Doppler API Server Error"
                )
        else:
            return response.json()

    def post(self, endpoint: str, params: dict | None, json_data: dict | None, data: dict | None) -> dict:
        """HTTP POST request

        :param endpoint: api url
        :param params: params dictionary
        :param json_data: json data
        :param data: data
        :return: response json data
        """
        session = self.sessions()
        response = session.post(url=endpoint, params=params, json=json_data, data=data)
        if not response.is_success:
            if not response.is_server_error:
                raise PydopplerError(
                    status_code=response.status_code,
                    message=response.json()["message"]
                )
            else:
                raise PydopplerError(
                    status_code=response.status_code,
                    message="Doppler API Server Error"
                )
        else:
            return response.json()
