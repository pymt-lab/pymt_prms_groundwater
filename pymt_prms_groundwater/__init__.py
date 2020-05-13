#! /usr/bin/env python

from .bmi import (PRMSGroundwater,
)

__all__ = ["PRMSGroundwater",
]

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
