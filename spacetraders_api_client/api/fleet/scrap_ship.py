from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.scrap_ship_response_200 import ScrapShipResponse200
from ...types import Response


def _get_kwargs(
    ship_symbol: str,
) -> Dict[str, Any]:

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/my/ships/{shipSymbol}/scrap".format(
            shipSymbol=ship_symbol,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ScrapShipResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ScrapShipResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ScrapShipResponse200]:
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
) -> Response[ScrapShipResponse200]:
    """Scrap Ship

     Scrap a ship, removing it from the game and returning a portion of the ship's value to the agent.
    The ship must be docked in a waypoint that has the `Shipyard` trait in order to use this function.
    To preview the amount of value that will be returned, use the Get Ship action.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScrapShipResponse200]
    """

    kwargs = _get_kwargs(
        ship_symbol=ship_symbol,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ship_symbol: str,
    *,
    client: AuthenticatedClient,
) -> Optional[ScrapShipResponse200]:
    """Scrap Ship

     Scrap a ship, removing it from the game and returning a portion of the ship's value to the agent.
    The ship must be docked in a waypoint that has the `Shipyard` trait in order to use this function.
    To preview the amount of value that will be returned, use the Get Ship action.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScrapShipResponse200
    """

    return sync_detailed(
        ship_symbol=ship_symbol,
        client=client,
    ).parsed


async def asyncio_detailed(
    ship_symbol: str,
    *,
    client: AuthenticatedClient,
) -> Response[ScrapShipResponse200]:
    """Scrap Ship

     Scrap a ship, removing it from the game and returning a portion of the ship's value to the agent.
    The ship must be docked in a waypoint that has the `Shipyard` trait in order to use this function.
    To preview the amount of value that will be returned, use the Get Ship action.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScrapShipResponse200]
    """

    kwargs = _get_kwargs(
        ship_symbol=ship_symbol,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ship_symbol: str,
    *,
    client: AuthenticatedClient,
) -> Optional[ScrapShipResponse200]:
    """Scrap Ship

     Scrap a ship, removing it from the game and returning a portion of the ship's value to the agent.
    The ship must be docked in a waypoint that has the `Shipyard` trait in order to use this function.
    To preview the amount of value that will be returned, use the Get Ship action.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScrapShipResponse200
    """

    return (
        await asyncio_detailed(
            ship_symbol=ship_symbol,
            client=client,
        )
    ).parsed
