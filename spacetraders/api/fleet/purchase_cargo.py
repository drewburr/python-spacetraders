from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.purchase_cargo_201_response import PurchaseCargo201Response
from ...models.purchase_cargo_request import PurchaseCargoRequest
from ...types import Response


def _get_kwargs(
    ship_symbol: str,
    *,
    json_body: PurchaseCargoRequest,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/my/ships/{shipSymbol}/purchase".format(
            shipSymbol=ship_symbol,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PurchaseCargo201Response]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = PurchaseCargo201Response.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PurchaseCargo201Response]:
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
    json_body: PurchaseCargoRequest,
) -> Response[PurchaseCargo201Response]:
    """Purchase Cargo

     Purchase cargo from a market.

    The ship must be docked in a waypoint that has `Marketplace` trait, and the market must be selling a
    good to be able to purchase it.

    The maximum amount of units of a good that can be purchased in each transaction are denoted by the
    `tradeVolume` value of the good, which can be viewed by using the Get Market action.

    Purchased goods are added to the ship's cargo hold.

    Args:
        ship_symbol (str):
        json_body (PurchaseCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseCargo201Response]
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
    json_body: PurchaseCargoRequest,
) -> Optional[PurchaseCargo201Response]:
    """Purchase Cargo

     Purchase cargo from a market.

    The ship must be docked in a waypoint that has `Marketplace` trait, and the market must be selling a
    good to be able to purchase it.

    The maximum amount of units of a good that can be purchased in each transaction are denoted by the
    `tradeVolume` value of the good, which can be viewed by using the Get Market action.

    Purchased goods are added to the ship's cargo hold.

    Args:
        ship_symbol (str):
        json_body (PurchaseCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PurchaseCargo201Response
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
    json_body: PurchaseCargoRequest,
) -> Response[PurchaseCargo201Response]:
    """Purchase Cargo

     Purchase cargo from a market.

    The ship must be docked in a waypoint that has `Marketplace` trait, and the market must be selling a
    good to be able to purchase it.

    The maximum amount of units of a good that can be purchased in each transaction are denoted by the
    `tradeVolume` value of the good, which can be viewed by using the Get Market action.

    Purchased goods are added to the ship's cargo hold.

    Args:
        ship_symbol (str):
        json_body (PurchaseCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseCargo201Response]
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
    json_body: PurchaseCargoRequest,
) -> Optional[PurchaseCargo201Response]:
    """Purchase Cargo

     Purchase cargo from a market.

    The ship must be docked in a waypoint that has `Marketplace` trait, and the market must be selling a
    good to be able to purchase it.

    The maximum amount of units of a good that can be purchased in each transaction are denoted by the
    `tradeVolume` value of the good, which can be viewed by using the Get Market action.

    Purchased goods are added to the ship's cargo hold.

    Args:
        ship_symbol (str):
        json_body (PurchaseCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PurchaseCargo201Response
    """

    return (
        await asyncio_detailed(
            ship_symbol=ship_symbol,
            client=client,
            json_body=json_body,
        )
    ).parsed
