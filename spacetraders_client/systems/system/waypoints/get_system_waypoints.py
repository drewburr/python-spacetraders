from spacetraders_api_client.api.systems.get_system_waypoints import sync_detailed as get

from spacetraders_api_client.models import get_system_waypoints_response_200
Class(name='GetSystemWaypointsResponse200', module_name='get_system_waypoints_response_200')
required_properties = 2


# name: get-system-waypoints
# identifier: get_system_waypoints
# path: ['systems', '{systemSymbol}', 'waypoints']
# tag: systems

# path: /systems/{systemSymbol}/waypoints
# method: get
# description: Return a paginated list of all of the waypoints for a given system.
# 
# If a waypoint is uncharted, it will return the `Uncharted` trait instead of its actual traits.
# name: get-system-waypoints
# requires_security: True
# summary: List Waypoints in System
# responses: module.endpoint.responses
# errors: []

