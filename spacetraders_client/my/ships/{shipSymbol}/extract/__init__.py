from spacetraders_api_client.api.fleet.extract_resources import sync_detailed as post

from spacetraders_api_client.models import extract_resources_response_201

# name: extract-resources
# identifier: extract_resources
# path: ['my', 'ships', '{shipSymbol}', 'extract']
# tag: fleet

# path: /my/ships/{shipSymbol}/extract
# method: post
# description: Extract resources from a waypoint that can be extracted, such as asteroid fields, into your ship. Send an optional survey as the payload to target specific yields.
# 
# The ship must be in orbit to be able to extract and must have mining equipments installed that can extract goods, such as the `Gas Siphon` mount for gas-based goods or `Mining Laser` mount for ore-based goods.
# 
# The survey property is now deprecated. See the `extract/survey` endpoint for more details.
# name: extract-resources
# requires_security: True
# summary: Extract Resources
# responses: module.endpoint.responses
# errors: []

