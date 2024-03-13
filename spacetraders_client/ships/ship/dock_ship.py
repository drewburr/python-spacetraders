from spacetraders_api_client.api.fleet.dock_ship import sync_detailed as post

from spacetraders_api_client.models import dock_ship_200_response
Class(name='DockShip200Response', module_name='dock_ship_200_response')
required_properties = 1


# name: dock-ship
# identifier: dock_ship
# path: ['ships', '{shipSymbol}', 'dock']
# tag: fleet

# path: /my/ships/{shipSymbol}/dock
# method: post
# description: Attempt to dock your ship at its current location. Docking will only succeed if your ship is capable of docking at the time of the request.
# 
# Docked ships can access elements in their current location, such as the market or a shipyard, but cannot do actions that require the ship to be above surface such as navigating or extracting.
# 
# The endpoint is idempotent - successive calls will succeed even if the ship is already docked.
# name: dock-ship
# requires_security: True
# summary: Dock Ship
# responses: module.endpoint.responses
# errors: []

