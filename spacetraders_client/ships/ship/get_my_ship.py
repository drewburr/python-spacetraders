from spacetraders_api_client.api.fleet.get_my_ship import sync_detailed as get

from spacetraders_api_client.models import get_my_ship_response_200
Class(name='GetMyShipResponse200', module_name='get_my_ship_response_200')
required_properties = 1


# name: get-my-ship
# identifier: get_my_ship
# path: ['ships', '{shipSymbol}']
# tag: fleet

# path: /my/ships/{shipSymbol}
# method: get
# description: Retrieve the details of a ship under your agent's ownership.
# name: get-my-ship
# requires_security: True
# summary: Get Ship
# responses: module.endpoint.responses
# errors: []

