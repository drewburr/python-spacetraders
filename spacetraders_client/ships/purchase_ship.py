from spacetraders_api_client.api.fleet.purchase_ship import sync_detailed as post

from spacetraders_api_client.models import purchase_ship_response_201
Class(name='PurchaseShipResponse201', module_name='purchase_ship_response_201')
required_properties = 1


# name: purchase-ship
# identifier: purchase_ship
# path: ['ships']
# tag: fleet

# path: /my/ships
# method: post
# description: Purchase a ship from a Shipyard. In order to use this function, a ship under your agent's ownership must be in a waypoint that has the `Shipyard` trait, and the Shipyard must sell the type of the desired ship.
# 
# Shipyards typically offer ship types, which are predefined templates of ships that have dedicated roles. A template comes with a preset of an engine, a reactor, and a frame. It may also include a few modules and mounts.
# name: purchase-ship
# requires_security: True
# summary: Purchase Ship
# responses: module.endpoint.responses
# errors: []

