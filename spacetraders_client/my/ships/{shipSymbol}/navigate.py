from spacetraders_api_client.api.fleet.navigate_ship import sync_detailed as post

from spacetraders_api_client.models import navigate_ship_response_200

# name: navigate-ship
# identifier: navigate_ship
# path: ['my', 'ships', '{shipSymbol}', 'navigate']
# tag: fleet

# path: /my/ships/{shipSymbol}/navigate
# method: post
# description: Navigate to a target destination. The ship must be in orbit to use this function. The destination waypoint must be within the same system as the ship's current location. Navigating will consume the necessary fuel from the ship's manifest based on the distance to the target waypoint.
# 
# The returned response will detail the route information including the expected time of arrival. Most ship actions are unavailable until the ship has arrived at it's destination.
# 
# To travel between systems, see the ship's Warp or Jump actions.
# name: navigate-ship
# requires_security: True
# summary: Navigate Ship
# responses: module.endpoint.responses
# errors: []

