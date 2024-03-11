from spacetraders_api_client.api.fleet.create_ship_system_scan import sync_detailed as post

from spacetraders_api_client.models import create_ship_system_scan_response_201

# name: create-ship-system-scan
# identifier: create_ship_system_scan
# path: ['my', 'ships', '{shipSymbol}', 'scan', 'systems']
# tag: fleet

# path: /my/ships/{shipSymbol}/scan/systems
# method: post
# description: Scan for nearby systems, retrieving information on the systems' distance from the ship and their waypoints. Requires a ship to have the `Sensor Array` mount installed to use.
# 
# The ship will enter a cooldown after using this function, during which it cannot execute certain actions.
# name: create-ship-system-scan
# requires_security: True
# summary: Scan Systems
# responses: module.endpoint.responses
# errors: []

