from pydoppler.types.auth import Tokens

from .validator import check_token


def basic_auth_header_value(doppler_token: Tokens) -> str: ...


def check_token():
    return None