from spacetraders_api_client.api.fleet.scrap_ship import sync_detailed as post

from spacetraders_api_client.models import scrap_ship_response_200
Class(name='ScrapShipResponse200', module_name='scrap_ship_response_200')
required_properties = 1


# name: scrap-ship
# identifier: scrap_ship
# path: ['ships', '{shipSymbol}', 'scrap']
# tag: fleet

# path: /my/ships/{shipSymbol}/scrap
# method: post
# description: Scrap a ship, removing it from the game and returning a portion of the ship's value to the agent. The ship must be docked in a waypoint that has the `Shipyard` trait in order to use this function. To preview the amount of value that will be returned, use the Get Ship action.
# name: scrap-ship
# requires_security: True
# summary: Scrap Ship
# responses: module.endpoint.responses
# errors: []

