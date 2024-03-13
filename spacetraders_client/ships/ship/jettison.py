from spacetraders_api_client.api.fleet.jettison import sync_detailed as post

from spacetraders_api_client.models import jettison_response_200
Class(name='JettisonResponse200', module_name='jettison_response_200')
required_properties = 1


# name: jettison
# identifier: jettison
# path: ['ships', '{shipSymbol}', 'jettison']
# tag: fleet

# path: /my/ships/{shipSymbol}/jettison
# method: post
# description: Jettison cargo from your ship's cargo hold.
# name: jettison
# requires_security: True
# summary: Jettison Cargo
# responses: module.endpoint.responses
# errors: []

