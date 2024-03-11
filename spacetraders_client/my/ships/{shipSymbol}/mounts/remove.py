from spacetraders_api_client.api.fleet.remove_mount import sync_detailed as post

from spacetraders_api_client.models import remove_mount_201_response

# name: remove-mount
# identifier: remove_mount
# path: ['my', 'ships', '{shipSymbol}', 'mounts', 'remove']
# tag: fleet

# path: /my/ships/{shipSymbol}/mounts/remove
# method: post
# description: Remove a mount from a ship.
# 
# The ship must be docked in a waypoint that has the `Shipyard` trait, and must have the desired mount that it wish to remove installed.
# 
# A removal fee will be deduced from the agent by the Shipyard.
# name: remove-mount
# requires_security: True
# summary: Remove Mount
# responses: module.endpoint.responses
# errors: []

