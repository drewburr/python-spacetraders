from spacetraders_api_client.api.fleet.transfer_cargo import sync_detailed as post

from spacetraders_api_client.models import transfer_cargo_200_response
Class(name='TransferCargo200Response', module_name='transfer_cargo_200_response')
required_properties = 1


# name: transfer-cargo
# identifier: transfer_cargo
# path: ['ships', '{shipSymbol}', 'transfer']
# tag: fleet

# path: /my/ships/{shipSymbol}/transfer
# method: post
# description: Transfer cargo between ships.
# 
# The receiving ship must be in the same waypoint as the transferring ship, and it must able to hold the additional cargo after the transfer is complete. Both ships also must be in the same state, either both are docked or both are orbiting.
# 
# The response body's cargo shows the cargo of the transferring ship after the transfer is complete.
# name: transfer-cargo
# requires_security: True
# summary: Transfer Cargo
# responses: module.endpoint.responses
# errors: []

