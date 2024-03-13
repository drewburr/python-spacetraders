from spacetraders_api_client.api.fleet.negotiate_contract import sync_detailed as post

from spacetraders_api_client.models import negotiate_contract_200_response
Class(name='NegotiateContract200Response', module_name='negotiate_contract_200_response')
required_properties = 1


# name: negotiateContract
# identifier: negotiate_contract
# path: ['ships', '{shipSymbol}', 'negotiate', 'contract']
# tag: fleet

# path: /my/ships/{shipSymbol}/negotiate/contract
# method: post
# description: Negotiate a new contract with the HQ.
# 
# In order to negotiate a new contract, an agent must not have ongoing or offered contracts over the allowed maximum amount. Currently the maximum contracts an agent can have at a time is 1.
# 
# Once a contract is negotiated, it is added to the list of contracts offered to the agent, which the agent can then accept. 
# 
# The ship must be present at any waypoint with a faction present to negotiate a contract with that faction.
# name: negotiateContract
# requires_security: True
# summary: Negotiate Contract
# responses: module.endpoint.responses
# errors: []

