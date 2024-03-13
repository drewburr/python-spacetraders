from spacetraders_api_client.api.fleet.orbit_ship import sync_detailed as post

from spacetraders_api_client.models import orbit_ship_200_response
Class(name='OrbitShip200Response', module_name='orbit_ship_200_response')
required_properties = 1


# name: orbit-ship
# identifier: orbit_ship
# path: ['ships', '{shipSymbol}', 'orbit']
# tag: fleet

# path: /my/ships/{shipSymbol}/orbit
# method: post
# description: Attempt to move your ship into orbit at its current location. The request will only succeed if your ship is capable of moving into orbit at the time of the request.
# 
# Orbiting ships are able to do actions that require the ship to be above surface such as navigating or extracting, but cannot access elements in their current waypoint, such as the market or a shipyard.
# 
# The endpoint is idempotent - successive calls will succeed even if the ship is already in orbit.
# name: orbit-ship
# requires_security: True
# summary: Orbit Ship
# responses: module.endpoint.responses
# errors: []

