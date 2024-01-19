from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sell_cargo_201_response import SellCargo201Response
from ...models.sell_cargo_request import SellCargoRequest
from ...types import Response


def _get_kwargs(
    ship_symbol: str,
    *,
    json_body: SellCargoRequest,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/my/ships/{shipSymbol}/sell".format(
            shipSymbol=ship_symbol,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SellCargo201Response]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = SellCargo201Response.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SellCargo201Response]:
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
    json_body: SellCargoRequest,
) -> Response[SellCargo201Response]:
    """Sell Cargo

     Sell cargo in your ship to a market that trades this cargo. The ship must be docked in a waypoint
    that has the `Marketplace` trait in order to use this function.

    Args:
        ship_symbol (str):
        json_body (SellCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SellCargo201Response]
    """

    kwargs = _get_kwargs(
        ship_symbol=ship_symbol,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ship_symbol: str,
    *,
    client: AuthenticatedClient,
    json_body: SellCargoRequest,
) -> Optional[SellCargo201Response]:
    """Sell Cargo

     Sell cargo in your ship to a market that trades this cargo. The ship must be docked in a waypoint
    that has the `Marketplace` trait in order to use this function.

    Args:
        ship_symbol (str):
        json_body (SellCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SellCargo201Response
    """

    return sync_detailed(
        ship_symbol=ship_symbol,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    ship_symbol: str,
    *,
    client: AuthenticatedClient,
    json_body: SellCargoRequest,
) -> Response[SellCargo201Response]:
    """Sell Cargo

     Sell cargo in your ship to a market that trades this cargo. The ship must be docked in a waypoint
    that has the `Marketplace` trait in order to use this function.

    Args:
        ship_symbol (str):
        json_body (SellCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SellCargo201Response]
    """

    kwargs = _get_kwargs(
        ship_symbol=ship_symbol,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ship_symbol: str,
    *,
    client: AuthenticatedClient,
    json_body: SellCargoRequest,
) -> Optional[SellCargo201Response]:
    """Sell Cargo

     Sell cargo in your ship to a market that trades this cargo. The ship must be docked in a waypoint
    that has the `Marketplace` trait in order to use this function.

    Args:
        ship_symbol (str):
        json_body (SellCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SellCargo201Response
    """

    return (
        await asyncio_detailed(
            ship_symbol=ship_symbol,
            client=client,
            json_body=json_body,
        )
    ).parsed
