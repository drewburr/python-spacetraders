""" Contains modules for accessing the API """

from . import get_status, register


class Default:
    get_status = get_status
    register = register


__all__ = "Default"
