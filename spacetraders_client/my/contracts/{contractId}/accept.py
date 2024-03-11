from spacetraders_api_client.api.contracts.accept_contract import sync_detailed as post

from spacetraders_api_client.models import accept_contract_response_200

# name: accept-contract
# identifier: accept_contract
# path: ['my', 'contracts', '{contractId}', 'accept']
# tag: contracts

# path: /my/contracts/{contractId}/accept
# method: post
# description: Accept a contract by ID. 
# 
# You can only accept contracts that were offered to you, were not accepted yet, and whose deadlines has not passed yet.
# name: accept-contract
# requires_security: True
# summary: Accept Contract
# responses: module.endpoint.responses
# errors: []

