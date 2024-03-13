from spacetraders_api_client.api.fleet.get_ship_cooldown import sync_detailed as get

from spacetraders_api_client.models import get_ship_cooldown_response_200
Class(name='GetShipCooldownResponse200', module_name='get_ship_cooldown_response_200')
required_properties = 1


# name: get-ship-cooldown
# identifier: get_ship_cooldown
# path: ['ships', '{shipSymbol}', 'cooldown']
# tag: fleet

# path: /my/ships/{shipSymbol}/cooldown
# method: get
# description: Retrieve the details of your ship's reactor cooldown. Some actions such as activating your jump drive, scanning, or extracting resources taxes your reactor and results in a cooldown.
# 
# Your ship cannot perform additional actions until your cooldown has expired. The duration of your cooldown is relative to the power consumption of the related modules or mounts for the action taken.
# 
# Response returns a 204 status code (no-content) when the ship has no cooldown.
# name: get-ship-cooldown
# requires_security: True
# summary: Get Ship Cooldown
# responses: module.endpoint.responses
# errors: []



# name: get-ship-cooldown
# identifier: get_ship_cooldown
# path: ['ships', '{shipSymbol}', 'cooldown']
# tag: fleet

# path: /my/ships/{shipSymbol}/cooldown
# method: get
# description: Retrieve the details of your ship's reactor cooldown. Some actions such as activating your jump drive, scanning, or extracting resources taxes your reactor and results in a cooldown.
# 
# Your ship cannot perform additional actions until your cooldown has expired. The duration of your cooldown is relative to the power consumption of the related modules or mounts for the action taken.
# 
# Response returns a 204 status code (no-content) when the ship has no cooldown.
# name: get-ship-cooldown
# requires_security: True
# summary: Get Ship Cooldown
# responses: module.endpoint.responses
# errors: []

