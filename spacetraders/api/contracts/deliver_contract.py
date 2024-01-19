from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deliver_contract_json_body import DeliverContractJsonBody
from ...models.deliver_contract_response_200 import DeliverContractResponse200
from ...types import Response


def _get_kwargs(
    contract_id: str,
    *,
    json_body: DeliverContractJsonBody,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/my/contracts/{contractId}/deliver".format(
            contractId=contract_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DeliverContractResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeliverContractResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DeliverContractResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    contract_id: str,
    *,
    client: AuthenticatedClient,
    json_body: DeliverContractJsonBody,
) -> Response[DeliverContractResponse200]:
    """Deliver Cargo to Contract

     Deliver cargo to a contract.

    In order to use this API, a ship must be at the delivery location (denoted in the delivery terms as
    `destinationSymbol` of a contract) and must have a number of units of a good required by this
    contract in its cargo.

    Cargo that was delivered will be removed from the ship's cargo.

    Args:
        contract_id (str):
        json_body (DeliverContractJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeliverContractResponse200]
    """

    kwargs = _get_kwargs(
        contract_id=contract_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    contract_id: str,
    *,
    client: AuthenticatedClient,
    json_body: DeliverContractJsonBody,
) -> Optional[DeliverContractResponse200]:
    """Deliver Cargo to Contract

     Deliver cargo to a contract.

    In order to use this API, a ship must be at the delivery location (denoted in the delivery terms as
    `destinationSymbol` of a contract) and must have a number of units of a good required by this
    contract in its cargo.

    Cargo that was delivered will be removed from the ship's cargo.

    Args:
        contract_id (str):
        json_body (DeliverContractJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeliverContractResponse200
    """

    return sync_detailed(
        contract_id=contract_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    contract_id: str,
    *,
    client: AuthenticatedClient,
    json_body: DeliverContractJsonBody,
) -> Response[DeliverContractResponse200]:
    """Deliver Cargo to Contract

     Deliver cargo to a contract.

    In order to use this API, a ship must be at the delivery location (denoted in the delivery terms as
    `destinationSymbol` of a contract) and must have a number of units of a good required by this
    contract in its cargo.

    Cargo that was delivered will be removed from the ship's cargo.

    Args:
        contract_id (str):
        json_body (DeliverContractJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeliverContractResponse200]
    """

    kwargs = _get_kwargs(
        contract_id=contract_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    contract_id: str,
    *,
    client: AuthenticatedClient,
    json_body: DeliverContractJsonBody,
) -> Optional[DeliverContractResponse200]:
    """Deliver Cargo to Contract

     Deliver cargo to a contract.

    In order to use this API, a ship must be at the delivery location (denoted in the delivery terms as
    `destinationSymbol` of a contract) and must have a number of units of a good required by this
    contract in its cargo.

    Cargo that was delivered will be removed from the ship's cargo.

    Args:
        contract_id (str):
        json_body (DeliverContractJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeliverContractResponse200
    """

    return (
        await asyncio_detailed(
            contract_id=contract_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
