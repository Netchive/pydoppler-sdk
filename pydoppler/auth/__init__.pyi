from base64 import b64encode
from pydoppler.types.auth import Tokens

def basic_auth_header_value(doppler_token: Tokens) -> str:...