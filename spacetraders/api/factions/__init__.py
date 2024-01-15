""" Contains methods for accessing the API """


from .get_faction import asyncio_detailed as get_faction_asyncio
from .get_faction import sync_detailed as get_faction
from .get_factions import asyncio_detailed as get_factions_asyncio
from .get_factions import sync_detailed as get_factions


class Factions:
    get_factions = get_factions
    get_faction = get_faction


class AsyncFactions:
    get_factions = get_factions_asyncio
    get_faction = get_faction_asyncio


__all__ = ("Factions", "AsyncFactions")
