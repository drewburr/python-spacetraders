from spacetraders_api_client.api.systems.get_waypoint import sync_detailed as get

from spacetraders_api_client.models import get_waypoint_response_200

# name: get-waypoint
# identifier: get_waypoint
# path: ['systems', '{systemSymbol}', 'waypoints', '{waypointSymbol}']
# tag: systems

# path: /systems/{systemSymbol}/waypoints/{waypointSymbol}
# method: get
# description: View the details of a waypoint.
# 
# If the waypoint is uncharted, it will return the 'Uncharted' trait instead of its actual traits.
# name: get-waypoint
# requires_security: True
# summary: Get Waypoint
# responses: module.endpoint.responses
# errors: []

