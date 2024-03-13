from spacetraders_api_client.api.fleet.get_ship_nav import sync_detailed as get

from spacetraders_api_client.models import get_ship_nav_response_200
Class(name='GetShipNavResponse200', module_name='get_ship_nav_response_200')
required_properties = 1


# name: get-ship-nav
# identifier: get_ship_nav
# path: ['ships', '{shipSymbol}', 'nav']
# tag: fleet

# path: /my/ships/{shipSymbol}/nav
# method: get
# description: Get the current nav status of a ship.
# name: get-ship-nav
# requires_security: True
# summary: Get Ship Nav
# responses: module.endpoint.responses
# errors: []

