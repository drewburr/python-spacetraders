from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_ship_nav_json_body import PatchShipNavJsonBody
from ...models.patch_ship_nav_response_200 import PatchShipNavResponse200
from ...types import Response


def _get_kwargs(
    ship_symbol: str,
    *,
    json_body: PatchShipNavJsonBody,
) -> Dict[str, Any]:
    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": "/my/ships/{shipSymbol}/nav".format(
            shipSymbol=ship_symbol,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PatchShipNavResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PatchShipNavResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PatchShipNavResponse200]:
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
    json_body: PatchShipNavJsonBody,
) -> Response[PatchShipNavResponse200]:
    """Patch Ship Nav

     Update the nav configuration of a ship.

    Currently only supports configuring the Flight Mode of the ship, which affects its speed and fuel
    consumption.

    Args:
        ship_symbol (str):
        json_body (PatchShipNavJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchShipNavResponse200]
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
    json_body: PatchShipNavJsonBody,
) -> Optional[PatchShipNavResponse200]:
    """Patch Ship Nav

     Update the nav configuration of a ship.

    Currently only supports configuring the Flight Mode of the ship, which affects its speed and fuel
    consumption.

    Args:
        ship_symbol (str):
        json_body (PatchShipNavJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchShipNavResponse200
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
    json_body: PatchShipNavJsonBody,
) -> Response[PatchShipNavResponse200]:
    """Patch Ship Nav

     Update the nav configuration of a ship.

    Currently only supports configuring the Flight Mode of the ship, which affects its speed and fuel
    consumption.

    Args:
        ship_symbol (str):
        json_body (PatchShipNavJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchShipNavResponse200]
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
    json_body: PatchShipNavJsonBody,
) -> Optional[PatchShipNavResponse200]:
    """Patch Ship Nav

     Update the nav configuration of a ship.

    Currently only supports configuring the Flight Mode of the ship, which affects its speed and fuel
    consumption.

    Args:
        ship_symbol (str):
        json_body (PatchShipNavJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchShipNavResponse200
    """

    return (
        await asyncio_detailed(
            ship_symbol=ship_symbol,
            client=client,
            json_body=json_body,
        )
    ).parsed
