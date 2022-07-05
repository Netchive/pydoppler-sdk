from httpx._auth import to_bytes
from base64 import b64encode
from pydoppler.types.auth import Tokens


def basic_auth_header_value(doppler_token: Tokens) -> str:
    token = b64encode(to_bytes(doppler_token + ':')).decode()
    return f"Basic {token}"
