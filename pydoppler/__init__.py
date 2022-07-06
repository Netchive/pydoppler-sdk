"""
Copyright (c) 2022, the NETCHIVE and Contributors. All rights reserved.
The full copyright notice can be found in the file LICENSE.
"""

__version__ = "0.1.0"

from pydoppler.doppler import Doppler as _Doppler

Doppler = _Doppler

__all__ = ["Doppler"]
