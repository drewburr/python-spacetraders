from spacetraders_api_client.api.fleet.siphon_resources import sync_detailed as post

from spacetraders_api_client.models import siphon_resources_response_201

# name: siphon-resources
# identifier: siphon_resources
# path: ['my', 'ships', '{shipSymbol}', 'siphon']
# tag: fleet

# path: /my/ships/{shipSymbol}/siphon
# method: post
# description: Siphon gases, such as hydrocarbon, from gas giants.
# 
# The ship must be in orbit to be able to siphon and must have siphon mounts and a gas processor installed.
# name: siphon-resources
# requires_security: True
# summary: Siphon Resources
# responses: module.endpoint.responses
# errors: []

