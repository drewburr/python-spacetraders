""" Contains methods for accessing the API """

from . import get_faction, get_factions


class Factions:
    get_factions = get_factions
    get_faction = get_faction


__all__ = "Factions"
