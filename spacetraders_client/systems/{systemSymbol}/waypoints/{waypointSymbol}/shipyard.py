from spacetraders_api_client.api.systems.get_shipyard import sync_detailed as get

from spacetraders_api_client.models import get_shipyard_response_200

# name: get-shipyard
# identifier: get_shipyard
# path: ['systems', '{systemSymbol}', 'waypoints', '{waypointSymbol}', 'shipyard']
# tag: systems

# path: /systems/{systemSymbol}/waypoints/{waypointSymbol}/shipyard
# method: get
# description: Get the shipyard for a waypoint. Requires a waypoint that has the `Shipyard` trait to use. Send a ship to the waypoint to access data on ships that are currently available for purchase and recent transactions.
# name: get-shipyard
# requires_security: True
# summary: Get Shipyard
# responses: module.endpoint.responses
# errors: []

