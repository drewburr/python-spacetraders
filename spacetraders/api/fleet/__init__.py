""" Contains methods for accessing the API """

from . import (
    create_chart,
    create_ship_ship_scan,
    create_ship_system_scan,
    create_ship_waypoint_scan,
    create_survey,
    dock_ship,
    extract_resources,
    extract_resources_with_survey,
    get_mounts,
    get_my_ship,
    get_my_ship_cargo,
    get_my_ships,
    get_ship_cooldown,
    get_ship_nav,
    install_mount,
    jettison,
    jump_ship,
    navigate_ship,
    negotiate_contract,
    orbit_ship,
    patch_ship_nav,
    purchase_cargo,
    purchase_ship,
    refuel_ship,
    remove_mount,
    sell_cargo,
    ship_refine,
    siphon_resources,
    transfer_cargo,
    warp_ship,
)


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


__all__ = "Fleet"
