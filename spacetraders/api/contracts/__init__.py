""" Contains methods for accessing the API """

from . import (
    accept_contract,
    deliver_contract,
    fulfill_contract,
    get_contract,
    get_contracts,
)


class Contracts:
    get_contracts = get_contracts
    get_contract = get_contract
    accept_contract = accept_contract
    deliver_contract = deliver_contract
    fulfill_contract = fulfill_contract


__all__ = "Contracts"
