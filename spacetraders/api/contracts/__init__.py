""" Contains methods for accessing the API """


from .accept_contract import asyncio_detailed as accept_contract_asyncio
from .accept_contract import sync_detailed as accept_contract
from .deliver_contract import asyncio_detailed as deliver_contract_asyncio
from .deliver_contract import sync_detailed as deliver_contract
from .fulfill_contract import asyncio_detailed as fulfill_contract_asyncio
from .fulfill_contract import sync_detailed as fulfill_contract
from .get_contract import asyncio_detailed as get_contract_asyncio
from .get_contract import sync_detailed as get_contract
from .get_contracts import asyncio_detailed as get_contracts_asyncio
from .get_contracts import sync_detailed as get_contracts


class Contracts:
    get_contracts = get_contracts
    get_contract = get_contract
    accept_contract = accept_contract
    deliver_contract = deliver_contract
    fulfill_contract = fulfill_contract


class AsyncContracts:
    get_contracts = get_contracts_asyncio
    get_contract = get_contract_asyncio
    accept_contract = accept_contract_asyncio
    deliver_contract = deliver_contract_asyncio
    fulfill_contract = fulfill_contract_asyncio


__all__ = ("Contracts", "AsyncContracts")
