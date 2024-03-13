from spacetraders_api_client.api.fleet.get_my_ship_cargo import sync_detailed as get

from spacetraders_api_client.models import get_my_ship_cargo_response_200
Class(name='GetMyShipCargoResponse200', module_name='get_my_ship_cargo_response_200')
required_properties = 1


# name: get-my-ship-cargo
# identifier: get_my_ship_cargo
# path: ['ships', '{shipSymbol}', 'cargo']
# tag: fleet

# path: /my/ships/{shipSymbol}/cargo
# method: get
# description: Retrieve the cargo of a ship under your agent's ownership.
# name: get-my-ship-cargo
# requires_security: True
# summary: Get Ship Cargo
# responses: module.endpoint.responses
# errors: []

