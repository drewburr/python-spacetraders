from spacetraders_api_client.api.fleet.create_ship_waypoint_scan import sync_detailed as post

from spacetraders_api_client.models import create_ship_waypoint_scan_response_201
Class(name='CreateShipWaypointScanResponse201', module_name='create_ship_waypoint_scan_response_201')
required_properties = 1


# name: create-ship-waypoint-scan
# identifier: create_ship_waypoint_scan
# path: ['ships', '{shipSymbol}', 'scan', 'waypoints']
# tag: fleet

# path: /my/ships/{shipSymbol}/scan/waypoints
# method: post
# description: Scan for nearby waypoints, retrieving detailed information on each waypoint in range. Scanning uncharted waypoints will allow you to ignore their uncharted state and will list the waypoints' traits.
# 
# Requires a ship to have the `Sensor Array` mount installed to use.
# 
# The ship will enter a cooldown after using this function, during which it cannot execute certain actions.
# name: create-ship-waypoint-scan
# requires_security: True
# summary: Scan Waypoints
# responses: module.endpoint.responses
# errors: []

