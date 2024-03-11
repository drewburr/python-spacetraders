from spacetraders_api_client.api.fleet.get_ship_nav import sync_detailed as get

from spacetraders_api_client.models import get_ship_nav_response_200

# name: get-ship-nav
# identifier: get_ship_nav
# path: ['my', 'ships', '{shipSymbol}', 'nav']
# tag: fleet

# path: /my/ships/{shipSymbol}/nav
# method: get
# description: Get the current nav status of a ship.
# name: get-ship-nav
# requires_security: True
# summary: Get Ship Nav
# responses: module.endpoint.responses
# errors: []

from spacetraders_api_client.api.fleet.patch_ship_nav import sync_detailed as patch

from spacetraders_api_client.models import patch_ship_nav_response_200

# name: patch-ship-nav
# identifier: patch_ship_nav
# path: ['my', 'ships', '{shipSymbol}', 'nav']
# tag: fleet

# path: /my/ships/{shipSymbol}/nav
# method: patch
# description: Update the nav configuration of a ship.
# 
# Currently only supports configuring the Flight Mode of the ship, which affects its speed and fuel consumption.
# name: patch-ship-nav
# requires_security: True
# summary: Patch Ship Nav
# responses: module.endpoint.responses
# errors: []

