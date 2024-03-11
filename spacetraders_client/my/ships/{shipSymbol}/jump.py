from spacetraders_api_client.api.fleet.jump_ship import sync_detailed as post

from spacetraders_api_client.models import jump_ship_response_200

# name: jump-ship
# identifier: jump_ship
# path: ['my', 'ships', '{shipSymbol}', 'jump']
# tag: fleet

# path: /my/ships/{shipSymbol}/jump
# method: post
# description: Jump your ship instantly to a target connected waypoint. The ship must be in orbit to execute a jump.
# 
# A unit of antimatter is purchased and consumed from the market when jumping. The price of antimatter is determined by the market and is subject to change. A ship can only jump to connected waypoints
# name: jump-ship
# requires_security: True
# summary: Jump Ship
# responses: module.endpoint.responses
# errors: []

