import re

from pydoppler.types.auth import AuditToken
from pydoppler.types.auth import CLIToken
from pydoppler.types.auth import PersonalToken
from pydoppler.types.auth import SCIMToken
from pydoppler.types.auth import ServiceToken


def check_personal_token(token: str) -> bool:
    """
    Check if the personal token is valid.

    :param token: The personal token to check.
    :return: True if the token is valid, False otherwise.
    """
    if re.match(r"/dp\.pt\.[a-zA-Z0-9]{40,44}/", token):
        return True
    else:
        return False


def check_service_token(token: str) -> bool:
    """
    Check if the service token is valid.

    :param token: The service token to check.
    :return: True if the token is valid, False otherwise.
    """
    if re.match(r"/dp\.st\.(?:[a-z0-9\-_]{2,35}\.)?[a-zA-Z0-9]{40,44}/", token):
        return True
    else:
        return False


def check_cli_token(token: str) -> bool:
    """
    Check if the CLI token is valid.

    :param token: The CLI token to check.
    :return: True if the token is valid, False otherwise.
    """
    if re.match(r"/dp\.ct\.[a-zA-Z0-9]{40,44}/", token):
        return True
    else:
        return False


def check_scim_token(token: str) -> bool:
    """
    Check if the SCIM token is valid.

    :param token: The SCIM token to check.
    :return: True if the token is valid, False otherwise.
    """
    if re.match(r"/dp\.scim\.[a-zA-Z0-9]{40,44}/", token):
        return True
    else:
        return False


def check_audit_token(token: str) -> bool:
    """
    Check if the audit token is valid.

    :param token: The audit token to check.
    :return: True if the token is valid, False otherwise.
    """
    if re.match(r"/dp\.audit\.[a-zA-Z0-9]{40,44}/", token):
        return True
    else:
        return False


def check_token(
    token: str,
) -> PersonalToken | ServiceToken | CLIToken | SCIMToken | AuditToken:
    """
    Check if the token is valid.

    :param token: The token to check.
    :return: True if the token is valid, False otherwise.
    """
    if check_personal_token(token):
        return PersonalToken(token)
    elif check_service_token(token):
        return ServiceToken(token)
    elif check_cli_token(token):
        return CLIToken(token)
    elif check_scim_token(token):
        return SCIMToken(token)
    elif check_audit_token(token):
        return AuditToken(token)
    else:
        raise TypeError("Invalid token type.")
