from spacetraders_api_client.api.systems.supply_construction import sync_detailed as post

from spacetraders_api_client.models import supply_construction_response_201
Class(name='SupplyConstructionResponse201', module_name='supply_construction_response_201')
required_properties = 1


# name: supply-construction
# identifier: supply_construction
# path: ['systems', '{systemSymbol}', 'waypoints', '{waypointSymbol}', 'construction', 'supply']
# tag: systems

# path: /systems/{systemSymbol}/waypoints/{waypointSymbol}/construction/supply
# method: post
# description: Supply a construction site with the specified good. Requires a waypoint with a property of `isUnderConstruction` to be true.
# 
# The good must be in your ship's cargo. The good will be removed from your ship's cargo and added to the construction site's materials.
# name: supply-construction
# requires_security: True
# summary: Supply Construction Site
# responses: module.endpoint.responses
# errors: []

