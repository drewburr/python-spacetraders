""" Contains methods for accessing the API """


from .create_chart import asyncio_detailed as create_chart_asyncio
from .create_chart import sync_detailed as create_chart
from .create_ship_ship_scan import asyncio_detailed as create_ship_ship_scan_asyncio
from .create_ship_ship_scan import sync_detailed as create_ship_ship_scan
from .create_ship_system_scan import asyncio_detailed as create_ship_system_scan_asyncio
from .create_ship_system_scan import sync_detailed as create_ship_system_scan
from .create_ship_waypoint_scan import (
    asyncio_detailed as create_ship_waypoint_scan_asyncio,
)
from .create_ship_waypoint_scan import sync_detailed as create_ship_waypoint_scan
from .create_survey import asyncio_detailed as create_survey_asyncio
from .create_survey import sync_detailed as create_survey
from .dock_ship import asyncio_detailed as dock_ship_asyncio
from .dock_ship import sync_detailed as dock_ship
from .extract_resources import asyncio_detailed as extract_resources_asyncio
from .extract_resources import sync_detailed as extract_resources
from .extract_resources_with_survey import (
    asyncio_detailed as extract_resources_with_survey_asyncio,
)
from .extract_resources_with_survey import (
    sync_detailed as extract_resources_with_survey,
)
from .get_mounts import asyncio_detailed as get_mounts_asyncio
from .get_mounts import sync_detailed as get_mounts
from .get_my_ship import asyncio_detailed as get_my_ship_asyncio
from .get_my_ship import sync_detailed as get_my_ship
from .get_my_ship_cargo import asyncio_detailed as get_my_ship_cargo_asyncio
from .get_my_ship_cargo import sync_detailed as get_my_ship_cargo
from .get_my_ships import asyncio_detailed as get_my_ships_asyncio
from .get_my_ships import sync_detailed as get_my_ships
from .get_ship_cooldown import asyncio_detailed as get_ship_cooldown_asyncio
from .get_ship_cooldown import sync_detailed as get_ship_cooldown
from .get_ship_nav import asyncio_detailed as get_ship_nav_asyncio
from .get_ship_nav import sync_detailed as get_ship_nav
from .install_mount import asyncio_detailed as install_mount_asyncio
from .install_mount import sync_detailed as install_mount
from .jettison import asyncio_detailed as jettison_asyncio
from .jettison import sync_detailed as jettison
from .jump_ship import asyncio_detailed as jump_ship_asyncio
from .jump_ship import sync_detailed as jump_ship
from .navigate_ship import asyncio_detailed as navigate_ship_asyncio
from .navigate_ship import sync_detailed as navigate_ship
from .negotiate_contract import asyncio_detailed as negotiate_contract_asyncio
from .negotiate_contract import sync_detailed as negotiate_contract
from .orbit_ship import asyncio_detailed as orbit_ship_asyncio
from .orbit_ship import sync_detailed as orbit_ship
from .patch_ship_nav import asyncio_detailed as patch_ship_nav_asyncio
from .patch_ship_nav import sync_detailed as patch_ship_nav
from .purchase_cargo import asyncio_detailed as purchase_cargo_asyncio
from .purchase_cargo import sync_detailed as purchase_cargo
from .purchase_ship import asyncio_detailed as purchase_ship_asyncio
from .purchase_ship import sync_detailed as purchase_ship
from .refuel_ship import asyncio_detailed as refuel_ship_asyncio
from .refuel_ship import sync_detailed as refuel_ship
from .remove_mount import asyncio_detailed as remove_mount_asyncio
from .remove_mount import sync_detailed as remove_mount
from .sell_cargo import asyncio_detailed as sell_cargo_asyncio
from .sell_cargo import sync_detailed as sell_cargo
from .ship_refine import asyncio_detailed as ship_refine_asyncio
from .ship_refine import sync_detailed as ship_refine
from .siphon_resources import asyncio_detailed as siphon_resources_asyncio
from .siphon_resources import sync_detailed as siphon_resources
from .transfer_cargo import asyncio_detailed as transfer_cargo_asyncio
from .transfer_cargo import sync_detailed as transfer_cargo
from .warp_ship import asyncio_detailed as warp_ship_asyncio
from .warp_ship import sync_detailed as warp_ship


class Fleet:
    get_my_ships = get_my_ships
    purchase_ship = purchase_ship
    get_my_ship = get_my_ship
    get_my_ship_cargo = get_my_ship_cargo
    orbit_ship = orbit_ship
    ship_refine = ship_refine
    create_chart = create_chart
    get_ship_cooldown = get_ship_cooldown
    dock_ship = dock_ship
    create_survey = create_survey
    extract_resources = extract_resources
    siphon_resources = siphon_resources
    extract_resources_with_survey = extract_resources_with_survey
    jettison = jettison
    jump_ship = jump_ship
    navigate_ship = navigate_ship
    get_ship_nav = get_ship_nav
    patch_ship_nav = patch_ship_nav
    warp_ship = warp_ship
    sell_cargo = sell_cargo
    create_ship_system_scan = create_ship_system_scan
    create_ship_waypoint_scan = create_ship_waypoint_scan
    create_ship_ship_scan = create_ship_ship_scan
    refuel_ship = refuel_ship
    purchase_cargo = purchase_cargo
    transfer_cargo = transfer_cargo
    negotiate_contract = negotiate_contract
    get_mounts = get_mounts
    install_mount = install_mount
    remove_mount = remove_mount


class AsyncFleet:
    get_my_ships = get_my_ships_asyncio
    purchase_ship = purchase_ship_asyncio
    get_my_ship = get_my_ship_asyncio
    get_my_ship_cargo = get_my_ship_cargo_asyncio
    orbit_ship = orbit_ship_asyncio
    ship_refine = ship_refine_asyncio
    create_chart = create_chart_asyncio
    get_ship_cooldown = get_ship_cooldown_asyncio
    dock_ship = dock_ship_asyncio
    create_survey = create_survey_asyncio
    extract_resources = extract_resources_asyncio
    siphon_resources = siphon_resources_asyncio
    extract_resources_with_survey = extract_resources_with_survey_asyncio
    jettison = jettison_asyncio
    jump_ship = jump_ship_asyncio
    navigate_ship = navigate_ship_asyncio
    get_ship_nav = get_ship_nav_asyncio
    patch_ship_nav = patch_ship_nav_asyncio
    warp_ship = warp_ship_asyncio
    sell_cargo = sell_cargo_asyncio
    create_ship_system_scan = create_ship_system_scan_asyncio
    create_ship_waypoint_scan = create_ship_waypoint_scan_asyncio
    create_ship_ship_scan = create_ship_ship_scan_asyncio
    refuel_ship = refuel_ship_asyncio
    purchase_cargo = purchase_cargo_asyncio
    transfer_cargo = transfer_cargo_asyncio
    negotiate_contract = negotiate_contract_asyncio
    get_mounts = get_mounts_asyncio
    install_mount = install_mount_asyncio
    remove_mount = remove_mount_asyncio


__all__ = ("Fleet", "AsyncFleet")
