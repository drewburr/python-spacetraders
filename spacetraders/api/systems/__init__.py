""" Contains methods for accessing the API """


from .get_construction import asyncio_detailed as get_construction_asyncio
from .get_construction import sync_detailed as get_construction
from .get_jump_gate import asyncio_detailed as get_jump_gate_asyncio
from .get_jump_gate import sync_detailed as get_jump_gate
from .get_market import asyncio_detailed as get_market_asyncio
from .get_market import sync_detailed as get_market
from .get_shipyard import asyncio_detailed as get_shipyard_asyncio
from .get_shipyard import sync_detailed as get_shipyard
from .get_system import asyncio_detailed as get_system_asyncio
from .get_system import sync_detailed as get_system
from .get_system_waypoints import asyncio_detailed as get_system_waypoints_asyncio
from .get_system_waypoints import sync_detailed as get_system_waypoints
from .get_systems import asyncio_detailed as get_systems_asyncio
from .get_systems import sync_detailed as get_systems
from .get_waypoint import asyncio_detailed as get_waypoint_asyncio
from .get_waypoint import sync_detailed as get_waypoint
from .supply_construction import asyncio_detailed as supply_construction_asyncio
from .supply_construction import sync_detailed as supply_construction


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


class AsyncSystems:
    get_systems = get_systems_asyncio
    get_system = get_system_asyncio
    get_system_waypoints = get_system_waypoints_asyncio
    get_waypoint = get_waypoint_asyncio
    get_market = get_market_asyncio
    get_shipyard = get_shipyard_asyncio
    get_jump_gate = get_jump_gate_asyncio
    get_construction = get_construction_asyncio
    supply_construction = supply_construction_asyncio


__all__ = ("Systems", "AsyncSystems")
