from spacetraders_api_client.api.contracts.deliver_contract import sync_detailed as post

from spacetraders_api_client.models import deliver_contract_response_200

# name: deliver-contract
# identifier: deliver_contract
# path: ['my', 'contracts', '{contractId}', 'deliver']
# tag: contracts

# path: /my/contracts/{contractId}/deliver
# method: post
# description: Deliver cargo to a contract.
# 
# In order to use this API, a ship must be at the delivery location (denoted in the delivery terms as `destinationSymbol` of a contract) and must have a number of units of a good required by this contract in its cargo.
# 
# Cargo that was delivered will be removed from the ship's cargo.
# name: deliver-contract
# requires_security: True
# summary: Deliver Cargo to Contract
# responses: module.endpoint.responses
# errors: []

