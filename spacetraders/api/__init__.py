from . import agents, contracts, default, factions, fleet, systems

class API(
    default.Default,
    systems.Systems,
    factions.Factions,
    agents.Agents,
    contracts.Contracts,
    fleet.Fleet,
):
    pass


__all__ = "API"
