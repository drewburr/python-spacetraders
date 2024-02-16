from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ship_refine_201_response import ShipRefine201Response
from ...models.ship_refine_json_body import ShipRefineJsonBody
from ...types import Response


def _get_kwargs(
    ship_symbol: str,
    *,
    json_body: ShipRefineJsonBody,
) -> Dict[str, Any]:

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/my/ships/{shipSymbol}/refine".format(
            shipSymbol=ship_symbol,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ShipRefine201Response]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = ShipRefine201Response.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ShipRefine201Response]:
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
    json_body: ShipRefineJsonBody,
) -> Response[ShipRefine201Response]:
    """Ship Refine

     Attempt to refine the raw materials on your ship. The request will only succeed if your ship is
    capable of refining at the time of the request. In order to be able to refine, a ship must have
    goods that can be refined and have installed a `Refinery` module that can refine it.

    When refining, 30 basic goods will be converted into 10 processed goods.

    Args:
        ship_symbol (str):
        json_body (ShipRefineJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ShipRefine201Response]
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
    json_body: ShipRefineJsonBody,
) -> Optional[ShipRefine201Response]:
    """Ship Refine

     Attempt to refine the raw materials on your ship. The request will only succeed if your ship is
    capable of refining at the time of the request. In order to be able to refine, a ship must have
    goods that can be refined and have installed a `Refinery` module that can refine it.

    When refining, 30 basic goods will be converted into 10 processed goods.

    Args:
        ship_symbol (str):
        json_body (ShipRefineJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ShipRefine201Response
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
    json_body: ShipRefineJsonBody,
) -> Response[ShipRefine201Response]:
    """Ship Refine

     Attempt to refine the raw materials on your ship. The request will only succeed if your ship is
    capable of refining at the time of the request. In order to be able to refine, a ship must have
    goods that can be refined and have installed a `Refinery` module that can refine it.

    When refining, 30 basic goods will be converted into 10 processed goods.

    Args:
        ship_symbol (str):
        json_body (ShipRefineJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ShipRefine201Response]
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
    json_body: ShipRefineJsonBody,
) -> Optional[ShipRefine201Response]:
    """Ship Refine

     Attempt to refine the raw materials on your ship. The request will only succeed if your ship is
    capable of refining at the time of the request. In order to be able to refine, a ship must have
    goods that can be refined and have installed a `Refinery` module that can refine it.

    When refining, 30 basic goods will be converted into 10 processed goods.

    Args:
        ship_symbol (str):
        json_body (ShipRefineJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ShipRefine201Response
    """

    return (
        await asyncio_detailed(
            ship_symbol=ship_symbol,
            client=client,
            json_body=json_body,
        )
    ).parsed
