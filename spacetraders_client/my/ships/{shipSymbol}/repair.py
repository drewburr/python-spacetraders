from spacetraders_api_client.api.fleet.get_repair_ship import sync_detailed as get

from spacetraders_api_client.models import get_repair_ship_response_200

# name: get-repair-ship
# identifier: get_repair_ship
# path: ['my', 'ships', '{shipSymbol}', 'repair']
# tag: fleet

# path: /my/ships/{shipSymbol}/repair
# method: get
# description: Get the cost of repairing a ship.
# name: get-repair-ship
# requires_security: True
# summary: Get Repair Ship
# responses: module.endpoint.responses
# errors: []

from spacetraders_api_client.api.fleet.repair_ship import sync_detailed as post

from spacetraders_api_client.models import repair_ship_response_200

# name: repair-ship
# identifier: repair_ship
# path: ['my', 'ships', '{shipSymbol}', 'repair']
# tag: fleet

# path: /my/ships/{shipSymbol}/repair
# method: post
# description: Repair a ship, restoring the ship to maximum condition. The ship must be docked at a waypoint that has the `Shipyard` trait in order to use this function. To preview the cost of repairing the ship, use the Get action.
# name: repair-ship
# requires_security: True
# summary: Repair Ship
# responses: module.endpoint.responses
# errors: []

