from typing import NewType, Union


PersonalToken = NewType("PersonalToken", str)
ServiceToken = NewType("ServiceToken", str)
CLIToken = NewType("CLIToken", str)
SCIMToken = NewType("SCIMToken", str)
AuditToken = NewType("AuditToken", str)

Tokens = Union[PersonalToken | ServiceToken | CLIToken | SCIMToken | AuditToken]

__all__ = [
    "PersonalToken",
    "ServiceToken",
    "CLIToken",
    "SCIMToken",
    "AuditToken",
    "Tokens",
]
