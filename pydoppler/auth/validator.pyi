from pydoppler.types.auth import AuditToken
from pydoppler.types.auth import CLIToken
from pydoppler.types.auth import PersonalToken
from pydoppler.types.auth import SCIMToken
from pydoppler.types.auth import ServiceToken


def check_personal_token(token: str) -> bool: ...
def check_service_token(token: str) -> bool: ...
def check_cli_token(token: str) -> bool: ...
def check_scim_token(token: str) -> bool: ...
def check_audit_token(token: str) -> bool: ...
def check_token(
    token: str,
) -> PersonalToken | ServiceToken | CLIToken | SCIMToken | AuditToken: ...