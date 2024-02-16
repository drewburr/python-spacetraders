from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.transfer_cargo_200_response import TransferCargo200Response
from ...models.transfer_cargo_request import TransferCargoRequest
from ...types import Response


def _get_kwargs(
    ship_symbol: str,
    *,
    body: TransferCargoRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/my/ships/{shipSymbol}/transfer".format(
            shipSymbol=ship_symbol,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TransferCargo200Response]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TransferCargo200Response.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[TransferCargo200Response]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ship_symbol: str,
    *,
    client: AuthenticatedClient,
    body: TransferCargoRequest,
) -> Response[TransferCargo200Response]:
    """Transfer Cargo

     Transfer cargo between ships.

    The receiving ship must be in the same waypoint as the transferring ship, and it must able to hold
    the additional cargo after the transfer is complete. Both ships also must be in the same state,
    either both are docked or both are orbiting.

    The response body's cargo shows the cargo of the transferring ship after the transfer is complete.

    Args:
        ship_symbol (str):
        body (TransferCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransferCargo200Response]
    """

    kwargs = _get_kwargs(
        ship_symbol=ship_symbol,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ship_symbol: str,
    *,
    client: AuthenticatedClient,
    body: TransferCargoRequest,
) -> Optional[TransferCargo200Response]:
    """Transfer Cargo

     Transfer cargo between ships.

    The receiving ship must be in the same waypoint as the transferring ship, and it must able to hold
    the additional cargo after the transfer is complete. Both ships also must be in the same state,
    either both are docked or both are orbiting.

    The response body's cargo shows the cargo of the transferring ship after the transfer is complete.

    Args:
        ship_symbol (str):
        body (TransferCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransferCargo200Response
    """

    return sync_detailed(
        ship_symbol=ship_symbol,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    ship_symbol: str,
    *,
    client: AuthenticatedClient,
    body: TransferCargoRequest,
) -> Response[TransferCargo200Response]:
    """Transfer Cargo

     Transfer cargo between ships.

    The receiving ship must be in the same waypoint as the transferring ship, and it must able to hold
    the additional cargo after the transfer is complete. Both ships also must be in the same state,
    either both are docked or both are orbiting.

    The response body's cargo shows the cargo of the transferring ship after the transfer is complete.

    Args:
        ship_symbol (str):
        body (TransferCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransferCargo200Response]
    """

    kwargs = _get_kwargs(
        ship_symbol=ship_symbol,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ship_symbol: str,
    *,
    client: AuthenticatedClient,
    body: TransferCargoRequest,
) -> Optional[TransferCargo200Response]:
    """Transfer Cargo

     Transfer cargo between ships.

    The receiving ship must be in the same waypoint as the transferring ship, and it must able to hold
    the additional cargo after the transfer is complete. Both ships also must be in the same state,
    either both are docked or both are orbiting.

    The response body's cargo shows the cargo of the transferring ship after the transfer is complete.

    Args:
        ship_symbol (str):
        body (TransferCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransferCargo200Response
    """

    return (
        await asyncio_detailed(
            ship_symbol=ship_symbol,
            client=client,
            body=body,
        )
    ).parsed
