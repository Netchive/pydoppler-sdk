from typing import NewType


PersonalToken = NewType("PersonalToken", str)
ServiceToken = NewType("ServiceToken", str)
CLIToken = NewType("CLIToken", str)
SCIMToken = NewType("SCIMToken", str)
AuditToken = NewType("AuditToken", str)

Tokens = PersonalToken | ServiceToken | CLIToken | SCIMToken | AuditToken

__all__ = [
    "PersonalToken",
    "ServiceToken",
    "CLIToken",
    "SCIMToken",
    "AuditToken",
    "Tokens",
]
