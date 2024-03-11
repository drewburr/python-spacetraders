from spacetraders_api_client.api.fleet.create_ship_ship_scan import sync_detailed as post

from spacetraders_api_client.models import create_ship_ship_scan_response_201

# name: create-ship-ship-scan
# identifier: create_ship_ship_scan
# path: ['my', 'ships', '{shipSymbol}', 'scan', 'ships']
# tag: fleet

# path: /my/ships/{shipSymbol}/scan/ships
# method: post
# description: Scan for nearby ships, retrieving information for all ships in range.
# 
# Requires a ship to have the `Sensor Array` mount installed to use.
# 
# The ship will enter a cooldown after using this function, during which it cannot execute certain actions.
# name: create-ship-ship-scan
# requires_security: True
# summary: Scan Ships
# responses: module.endpoint.responses
# errors: []

