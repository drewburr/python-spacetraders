from spacetraders_api_client.api.contracts.fulfill_contract import sync_detailed as post

from spacetraders_api_client.models import fulfill_contract_response_200

# name: fulfill-contract
# identifier: fulfill_contract
# path: ['my', 'contracts', '{contractId}', 'fulfill']
# tag: contracts

# path: /my/contracts/{contractId}/fulfill
# method: post
# description: Fulfill a contract. Can only be used on contracts that have all of their delivery terms fulfilled.
# name: fulfill-contract
# requires_security: True
# summary: Fulfill Contract
# responses: module.endpoint.responses
# errors: []

