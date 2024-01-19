from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.orbit_ship_200_response import OrbitShip200Response
from ...types import Response


def _get_kwargs(
    ship_symbol: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/my/ships/{shipSymbol}/orbit".format(
            shipSymbol=ship_symbol,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OrbitShip200Response]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OrbitShip200Response.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OrbitShip200Response]:
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
) -> Response[OrbitShip200Response]:
    """Orbit Ship

     Attempt to move your ship into orbit at its current location. The request will only succeed if your
    ship is capable of moving into orbit at the time of the request.

    Orbiting ships are able to do actions that require the ship to be above surface such as navigating
    or extracting, but cannot access elements in their current waypoint, such as the market or a
    shipyard.

    The endpoint is idempotent - successive calls will succeed even if the ship is already in orbit.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrbitShip200Response]
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
) -> Optional[OrbitShip200Response]:
    """Orbit Ship

     Attempt to move your ship into orbit at its current location. The request will only succeed if your
    ship is capable of moving into orbit at the time of the request.

    Orbiting ships are able to do actions that require the ship to be above surface such as navigating
    or extracting, but cannot access elements in their current waypoint, such as the market or a
    shipyard.

    The endpoint is idempotent - successive calls will succeed even if the ship is already in orbit.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrbitShip200Response
    """

    return sync_detailed(
        ship_symbol=ship_symbol,
        client=client,
    ).parsed


async def asyncio_detailed(
    ship_symbol: str,
    *,
    client: AuthenticatedClient,
) -> Response[OrbitShip200Response]:
    """Orbit Ship

     Attempt to move your ship into orbit at its current location. The request will only succeed if your
    ship is capable of moving into orbit at the time of the request.

    Orbiting ships are able to do actions that require the ship to be above surface such as navigating
    or extracting, but cannot access elements in their current waypoint, such as the market or a
    shipyard.

    The endpoint is idempotent - successive calls will succeed even if the ship is already in orbit.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrbitShip200Response]
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
) -> Optional[OrbitShip200Response]:
    """Orbit Ship

     Attempt to move your ship into orbit at its current location. The request will only succeed if your
    ship is capable of moving into orbit at the time of the request.

    Orbiting ships are able to do actions that require the ship to be above surface such as navigating
    or extracting, but cannot access elements in their current waypoint, such as the market or a
    shipyard.

    The endpoint is idempotent - successive calls will succeed even if the ship is already in orbit.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrbitShip200Response
    """

    return (
        await asyncio_detailed(
            ship_symbol=ship_symbol,
            client=client,
        )
    ).parsed
