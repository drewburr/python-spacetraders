from spacetraders_api_client.api.fleet.get_scrap_ship import sync_detailed as get

from spacetraders_api_client.models import get_scrap_ship_response_200
Class(name='GetScrapShipResponse200', module_name='get_scrap_ship_response_200')
required_properties = 1


# name: get-scrap-ship
# identifier: get_scrap_ship
# path: ['ships', '{shipSymbol}', 'scrap']
# tag: fleet

# path: /my/ships/{shipSymbol}/scrap
# method: get
# description: Get the amount of value that will be returned when scrapping a ship.
# name: get-scrap-ship
# requires_security: True
# summary: Get Scrap Ship
# responses: module.endpoint.responses
# errors: []

