from spacetraders_api_client.api.fleet.sell_cargo import sync_detailed as post

from spacetraders_api_client.models import sell_cargo_201_response

# name: sell-cargo
# identifier: sell_cargo
# path: ['my', 'ships', '{shipSymbol}', 'sell']
# tag: fleet

# path: /my/ships/{shipSymbol}/sell
# method: post
# description: Sell cargo in your ship to a market that trades this cargo. The ship must be docked in a waypoint that has the `Marketplace` trait in order to use this function.
# name: sell-cargo
# requires_security: True
# summary: Sell Cargo
# responses: module.endpoint.responses
# errors: []

