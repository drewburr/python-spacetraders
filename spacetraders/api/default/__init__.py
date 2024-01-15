""" Contains methods for accessing the API """


from .get_status import asyncio_detailed as get_status_asyncio
from .get_status import sync_detailed as get_status
from .register import asyncio_detailed as register_asyncio
from .register import sync_detailed as register


class Default:
    get_status = get_status
    register = register


class AsyncDefault:
    get_status = get_status_asyncio
    register = register_asyncio


__all__ = ("Default", "AsyncDefault")
