from base64 import b64encode

from httpx._auth import to_bytes
from pydoppler.auth.validator import check_token
from pydoppler.types.auth import Tokens


def basic_auth_header_value(doppler_token: Tokens) -> str:
    token = b64encode(to_bytes(doppler_token + ":")).decode()
    return f"Basic {token}"


__all__ = ["basic_auth_header_value", "validator"]
