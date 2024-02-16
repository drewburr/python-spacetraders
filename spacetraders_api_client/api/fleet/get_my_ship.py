from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_my_ship_response_200 import GetMyShipResponse200
from ...types import Response


def _get_kwargs(
    ship_symbol: str,
) -> Dict[str, Any]:
    return {
        "method": "get",
        "url": "/my/ships/{shipSymbol}".format(
            shipSymbol=ship_symbol,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetMyShipResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetMyShipResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetMyShipResponse200]:
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
) -> Response[GetMyShipResponse200]:
    """Get Ship

     Retrieve the details of a ship under your agent's ownership.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMyShipResponse200]
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
) -> Optional[GetMyShipResponse200]:
    """Get Ship

     Retrieve the details of a ship under your agent's ownership.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMyShipResponse200
    """

    return sync_detailed(
        ship_symbol=ship_symbol,
        client=client,
    ).parsed


async def asyncio_detailed(
    ship_symbol: str,
    *,
    client: AuthenticatedClient,
) -> Response[GetMyShipResponse200]:
    """Get Ship

     Retrieve the details of a ship under your agent's ownership.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMyShipResponse200]
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
) -> Optional[GetMyShipResponse200]:
    """Get Ship

     Retrieve the details of a ship under your agent's ownership.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMyShipResponse200
    """

    return (
        await asyncio_detailed(
            ship_symbol=ship_symbol,
            client=client,
        )
    ).parsed
