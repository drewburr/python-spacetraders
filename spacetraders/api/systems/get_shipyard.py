from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_shipyard_response_200 import GetShipyardResponse200
from ...types import Response


def _get_kwargs(
    system_symbol: str,
    waypoint_symbol: str,
) -> Dict[str, Any]:
    return {
        "method": "get",
        "url": "/systems/{systemSymbol}/waypoints/{waypointSymbol}/shipyard".format(
            systemSymbol=system_symbol,
            waypointSymbol=waypoint_symbol,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetShipyardResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetShipyardResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetShipyardResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    system_symbol: str,
    waypoint_symbol: str,
    *,
    client: AuthenticatedClient,
) -> Response[GetShipyardResponse200]:
    """Get Shipyard

     Get the shipyard for a waypoint. Requires a waypoint that has the `Shipyard` trait to use. Send a
    ship to the waypoint to access data on ships that are currently available for purchase and recent
    transactions.

    Args:
        system_symbol (str):
        waypoint_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShipyardResponse200]
    """

    kwargs = _get_kwargs(
        system_symbol=system_symbol,
        waypoint_symbol=waypoint_symbol,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_symbol: str,
    waypoint_symbol: str,
    *,
    client: AuthenticatedClient,
) -> Optional[GetShipyardResponse200]:
    """Get Shipyard

     Get the shipyard for a waypoint. Requires a waypoint that has the `Shipyard` trait to use. Send a
    ship to the waypoint to access data on ships that are currently available for purchase and recent
    transactions.

    Args:
        system_symbol (str):
        waypoint_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShipyardResponse200
    """

    return sync_detailed(
        system_symbol=system_symbol,
        waypoint_symbol=waypoint_symbol,
        client=client,
    ).parsed


async def asyncio_detailed(
    system_symbol: str,
    waypoint_symbol: str,
    *,
    client: AuthenticatedClient,
) -> Response[GetShipyardResponse200]:
    """Get Shipyard

     Get the shipyard for a waypoint. Requires a waypoint that has the `Shipyard` trait to use. Send a
    ship to the waypoint to access data on ships that are currently available for purchase and recent
    transactions.

    Args:
        system_symbol (str):
        waypoint_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShipyardResponse200]
    """

    kwargs = _get_kwargs(
        system_symbol=system_symbol,
        waypoint_symbol=waypoint_symbol,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_symbol: str,
    waypoint_symbol: str,
    *,
    client: AuthenticatedClient,
) -> Optional[GetShipyardResponse200]:
    """Get Shipyard

     Get the shipyard for a waypoint. Requires a waypoint that has the `Shipyard` trait to use. Send a
    ship to the waypoint to access data on ships that are currently available for purchase and recent
    transactions.

    Args:
        system_symbol (str):
        waypoint_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShipyardResponse200
    """

    return (
        await asyncio_detailed(
            system_symbol=system_symbol,
            waypoint_symbol=waypoint_symbol,
            client=client,
        )
    ).parsed
