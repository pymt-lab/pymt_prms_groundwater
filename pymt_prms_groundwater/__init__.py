#! /usr/bin/env python
import pkg_resources

__version__ = pkg_resources.get_distribution("pymt_prms_groundwater").version


from .bmi import PRMSGroundwater

__all__ = [
    "PRMSGroundwater",
]
