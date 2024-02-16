""" Contains modules for accessing the API """

from . import (
    get_construction,
    get_jump_gate,
    get_market,
    get_shipyard,
    get_system,
    get_system_waypoints,
    get_systems,
    get_waypoint,
    supply_construction,
)


class Systems:
    get_systems = get_systems
    get_system = get_system
    get_system_waypoints = get_system_waypoints
    get_waypoint = get_waypoint
    get_market = get_market
    get_shipyard = get_shipyard
    get_jump_gate = get_jump_gate
    get_construction = get_construction
    supply_construction = supply_construction


__all__ = "Systems"
