from spacetraders_api_client.api.fleet.install_mount import sync_detailed as post

from spacetraders_api_client.models import install_mount_201_response

# name: install-mount
# identifier: install_mount
# path: ['my', 'ships', '{shipSymbol}', 'mounts', 'install']
# tag: fleet

# path: /my/ships/{shipSymbol}/mounts/install
# method: post
# description: Install a mount on a ship.
# 
# In order to install a mount, the ship must be docked and located in a waypoint that has a `Shipyard` trait. The ship also must have the mount to install in its cargo hold.
# 
# An installation fee will be deduced by the Shipyard for installing the mount on the ship. 
# name: install-mount
# requires_security: True
# summary: Install Mount
# responses: module.endpoint.responses
# errors: []

