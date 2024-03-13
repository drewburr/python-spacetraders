from spacetraders_api_client.api.fleet.ship_refine import sync_detailed as post

from spacetraders_api_client.models import ship_refine_201_response
Class(name='ShipRefine201Response', module_name='ship_refine_201_response')
required_properties = 1


# name: ship-refine
# identifier: ship_refine
# path: ['ships', '{shipSymbol}', 'refine']
# tag: fleet

# path: /my/ships/{shipSymbol}/refine
# method: post
# description: Attempt to refine the raw materials on your ship. The request will only succeed if your ship is capable of refining at the time of the request. In order to be able to refine, a ship must have goods that can be refined and have installed a `Refinery` module that can refine it.
# 
# When refining, 30 basic goods will be converted into 10 processed goods.
# name: ship-refine
# requires_security: True
# summary: Ship Refine
# responses: module.endpoint.responses
# errors: []

