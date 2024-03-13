from spacetraders_api_client.api.systems.get_market import sync_detailed as get

from spacetraders_api_client.models import get_market_response_200
Class(name='GetMarketResponse200', module_name='get_market_response_200')
required_properties = 1


# name: get-market
# identifier: get_market
# path: ['systems', '{systemSymbol}', 'waypoints', '{waypointSymbol}', 'market']
# tag: systems

# path: /systems/{systemSymbol}/waypoints/{waypointSymbol}/market
# method: get
# description: Retrieve imports, exports and exchange data from a marketplace. Requires a waypoint that has the `Marketplace` trait to use.
# 
# Send a ship to the waypoint to access trade good prices and recent transactions. Refer to the [Market Overview page](https://docs.spacetraders.io/game-concepts/markets) to gain better a understanding of the market in the game.
# name: get-market
# requires_security: True
# summary: Get Market
# responses: module.endpoint.responses
# errors: []

