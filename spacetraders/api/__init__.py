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


class AsyncAPI(
    default.AsyncDefault,
    systems.AsyncSystems,
    factions.AsyncFactions,
    agents.AsyncAgents,
    contracts.AsyncContracts,
    fleet.AsyncFleet,
):
    pass


__all__ = ("API", "AsyncAPI")
