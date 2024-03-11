from spacetraders_api_client.api.systems.get_jump_gate import sync_detailed as get

from spacetraders_api_client.models import get_jump_gate_response_200

# name: get-jump-gate
# identifier: get_jump_gate
# path: ['systems', '{systemSymbol}', 'waypoints', '{waypointSymbol}', 'jump-gate']
# tag: systems

# path: /systems/{systemSymbol}/waypoints/{waypointSymbol}/jump-gate
# method: get
# description: Get jump gate details for a waypoint. Requires a waypoint of type `JUMP_GATE` to use.
# 
# Waypoints connected to this jump gate can be 
# name: get-jump-gate
# requires_security: True
# summary: Get Jump Gate
# responses: module.endpoint.responses
# errors: []

