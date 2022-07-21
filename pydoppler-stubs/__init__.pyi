from typing import Type

from .doppler import Doppler as _Doppler
from .doppler import DopplerAudit as _DopplerAudit


__version__: str

Doppler: Type[_Doppler]
DopplerAudit: Type[_DopplerAudit]
