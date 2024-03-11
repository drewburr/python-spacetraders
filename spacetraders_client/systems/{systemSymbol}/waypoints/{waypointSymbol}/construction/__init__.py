from spacetraders_api_client.api.systems.get_construction import sync_detailed as get

from spacetraders_api_client.models import get_construction_response_200

# name: get-construction
# identifier: get_construction
# path: ['systems', '{systemSymbol}', 'waypoints', '{waypointSymbol}', 'construction']
# tag: systems

# path: /systems/{systemSymbol}/waypoints/{waypointSymbol}/construction
# method: get
# description: Get construction details for a waypoint. Requires a waypoint with a property of `isUnderConstruction` to be true.
# name: get-construction
# requires_security: True
# summary: Get Construction Site
# responses: module.endpoint.responses
# errors: []

