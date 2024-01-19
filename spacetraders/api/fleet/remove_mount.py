from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remove_mount_201_response import RemoveMount201Response
from ...models.remove_mount_request import RemoveMountRequest
from ...types import Response


def _get_kwargs(
    ship_symbol: str,
    *,
    json_body: RemoveMountRequest,
) -> Dict[str, Any]:
    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/my/ships/{shipSymbol}/mounts/remove".format(
            shipSymbol=ship_symbol,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[RemoveMount201Response]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = RemoveMount201Response.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RemoveMount201Response]:
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
    json_body: RemoveMountRequest,
) -> Response[RemoveMount201Response]:
    """Remove Mount

     Remove a mount from a ship.

    The ship must be docked in a waypoint that has the `Shipyard` trait, and must have the desired mount
    that it wish to remove installed.

    A removal fee will be deduced from the agent by the Shipyard.

    Args:
        ship_symbol (str):
        json_body (RemoveMountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveMount201Response]
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
    json_body: RemoveMountRequest,
) -> Optional[RemoveMount201Response]:
    """Remove Mount

     Remove a mount from a ship.

    The ship must be docked in a waypoint that has the `Shipyard` trait, and must have the desired mount
    that it wish to remove installed.

    A removal fee will be deduced from the agent by the Shipyard.

    Args:
        ship_symbol (str):
        json_body (RemoveMountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveMount201Response
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
    json_body: RemoveMountRequest,
) -> Response[RemoveMount201Response]:
    """Remove Mount

     Remove a mount from a ship.

    The ship must be docked in a waypoint that has the `Shipyard` trait, and must have the desired mount
    that it wish to remove installed.

    A removal fee will be deduced from the agent by the Shipyard.

    Args:
        ship_symbol (str):
        json_body (RemoveMountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveMount201Response]
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
    json_body: RemoveMountRequest,
) -> Optional[RemoveMount201Response]:
    """Remove Mount

     Remove a mount from a ship.

    The ship must be docked in a waypoint that has the `Shipyard` trait, and must have the desired mount
    that it wish to remove installed.

    A removal fee will be deduced from the agent by the Shipyard.

    Args:
        ship_symbol (str):
        json_body (RemoveMountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveMount201Response
    """

    return (
        await asyncio_detailed(
            ship_symbol=ship_symbol,
            client=client,
            json_body=json_body,
        )
    ).parsed
