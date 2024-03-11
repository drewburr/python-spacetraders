from spacetraders_api_client.api.fleet.refuel_ship import sync_detailed as post

from spacetraders_api_client.models import refuel_ship_response_200

# name: refuel-ship
# identifier: refuel_ship
# path: ['my', 'ships', '{shipSymbol}', 'refuel']
# tag: fleet

# path: /my/ships/{shipSymbol}/refuel
# method: post
# description: Refuel your ship by buying fuel from the local market.
# 
# Requires the ship to be docked in a waypoint that has the `Marketplace` trait, and the market must be selling fuel in order to refuel.
# 
# Each fuel bought from the market replenishes 100 units in your ship's fuel.
# 
# Ships will always be refuel to their frame's maximum fuel capacity when using this action.
# name: refuel-ship
# requires_security: True
# summary: Refuel Ship
# responses: module.endpoint.responses
# errors: []

