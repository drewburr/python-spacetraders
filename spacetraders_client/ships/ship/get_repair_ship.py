from spacetraders_api_client.api.fleet.get_repair_ship import sync_detailed as get

from spacetraders_api_client.models import get_repair_ship_response_200
Class(name='GetRepairShipResponse200', module_name='get_repair_ship_response_200')
required_properties = 1


# name: get-repair-ship
# identifier: get_repair_ship
# path: ['ships', '{shipSymbol}', 'repair']
# tag: fleet

# path: /my/ships/{shipSymbol}/repair
# method: get
# description: Get the cost of repairing a ship.
# name: get-repair-ship
# requires_security: True
# summary: Get Repair Ship
# responses: module.endpoint.responses
# errors: []

