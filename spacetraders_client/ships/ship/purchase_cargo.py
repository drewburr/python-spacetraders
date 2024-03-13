from spacetraders_api_client.api.fleet.purchase_cargo import sync_detailed as post

from spacetraders_api_client.models import purchase_cargo_201_response
Class(name='PurchaseCargo201Response', module_name='purchase_cargo_201_response')
required_properties = 1


# name: purchase-cargo
# identifier: purchase_cargo
# path: ['ships', '{shipSymbol}', 'purchase']
# tag: fleet

# path: /my/ships/{shipSymbol}/purchase
# method: post
# description: Purchase cargo from a market.
# 
# The ship must be docked in a waypoint that has `Marketplace` trait, and the market must be selling a good to be able to purchase it.
# 
# The maximum amount of units of a good that can be purchased in each transaction are denoted by the `tradeVolume` value of the good, which can be viewed by using the Get Market action.
# 
# Purchased goods are added to the ship's cargo hold.
# name: purchase-cargo
# requires_security: True
# summary: Purchase Cargo
# responses: module.endpoint.responses
# errors: []

