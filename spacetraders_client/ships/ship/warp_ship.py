from spacetraders_api_client.api.fleet.warp_ship import sync_detailed as post

from spacetraders_api_client.models import warp_ship_response_200
Class(name='WarpShipResponse200', module_name='warp_ship_response_200')
required_properties = 1


# name: warp-ship
# identifier: warp_ship
# path: ['ships', '{shipSymbol}', 'warp']
# tag: fleet

# path: /my/ships/{shipSymbol}/warp
# method: post
# description: Warp your ship to a target destination in another system. The ship must be in orbit to use this function and must have the `Warp Drive` module installed. Warping will consume the necessary fuel from the ship's manifest.
# 
# The returned response will detail the route information including the expected time of arrival. Most ship actions are unavailable until the ship has arrived at its destination.
# name: warp-ship
# requires_security: True
# summary: Warp Ship
# responses: module.endpoint.responses
# errors: []

