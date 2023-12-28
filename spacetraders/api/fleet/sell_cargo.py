from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sell_cargo_sell_cargo_201_response import SellCargoSellCargo201Response
from ...models.sell_cargo_sell_cargo_request import SellCargoSellCargoRequest
from ...types import Response


def _get_kwargs(
    ship_symbol: str,
    *,
    json_body: SellCargoSellCargoRequest,
) -> Dict[str, Any]:
    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/my/ships/{shipSymbol}/sell".format(
            shipSymbol=ship_symbol,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SellCargoSellCargo201Response]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = SellCargoSellCargo201Response.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SellCargoSellCargo201Response]:
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
    json_body: SellCargoSellCargoRequest,
) -> Response[SellCargoSellCargo201Response]:
    """Sell Cargo

     Sell cargo in your ship to a market that trades this cargo. The ship must be docked in a waypoint
    that has the `Marketplace` trait in order to use this function.

    Args:
        ship_symbol (str):
        json_body (SellCargoSellCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SellCargoSellCargo201Response]
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
    json_body: SellCargoSellCargoRequest,
) -> Optional[SellCargoSellCargo201Response]:
    """Sell Cargo

     Sell cargo in your ship to a market that trades this cargo. The ship must be docked in a waypoint
    that has the `Marketplace` trait in order to use this function.

    Args:
        ship_symbol (str):
        json_body (SellCargoSellCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SellCargoSellCargo201Response
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
    json_body: SellCargoSellCargoRequest,
) -> Response[SellCargoSellCargo201Response]:
    """Sell Cargo

     Sell cargo in your ship to a market that trades this cargo. The ship must be docked in a waypoint
    that has the `Marketplace` trait in order to use this function.

    Args:
        ship_symbol (str):
        json_body (SellCargoSellCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SellCargoSellCargo201Response]
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
    json_body: SellCargoSellCargoRequest,
) -> Optional[SellCargoSellCargo201Response]:
    """Sell Cargo

     Sell cargo in your ship to a market that trades this cargo. The ship must be docked in a waypoint
    that has the `Marketplace` trait in order to use this function.

    Args:
        ship_symbol (str):
        json_body (SellCargoSellCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SellCargoSellCargo201Response
    """

    return (
        await asyncio_detailed(
            ship_symbol=ship_symbol,
            client=client,
            json_body=json_body,
        )
    ).parsed
