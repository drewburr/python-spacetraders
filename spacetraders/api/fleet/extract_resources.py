from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.extract_resources_json_body import ExtractResourcesJsonBody
from ...models.extract_resources_response_201 import ExtractResourcesResponse201
from ...types import Response


def _get_kwargs(
    ship_symbol: str,
    *,
    json_body: ExtractResourcesJsonBody,
) -> Dict[str, Any]:
    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/my/ships/{shipSymbol}/extract".format(
            shipSymbol=ship_symbol,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ExtractResourcesResponse201]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = ExtractResourcesResponse201.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ExtractResourcesResponse201]:
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
    json_body: ExtractResourcesJsonBody,
) -> Response[ExtractResourcesResponse201]:
    """Extract Resources

     Extract resources from a waypoint that can be extracted, such as asteroid fields, into your ship.
    Send an optional survey as the payload to target specific yields.

    The ship must be in orbit to be able to extract and must have mining equipments installed that can
    extract goods, such as the `Gas Siphon` mount for gas-based goods or `Mining Laser` mount for ore-
    based goods.

    The survey property is now deprecated. See the `extract/survey` endpoint for more details.

    Args:
        ship_symbol (str):
        json_body (ExtractResourcesJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExtractResourcesResponse201]
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
    json_body: ExtractResourcesJsonBody,
) -> Optional[ExtractResourcesResponse201]:
    """Extract Resources

     Extract resources from a waypoint that can be extracted, such as asteroid fields, into your ship.
    Send an optional survey as the payload to target specific yields.

    The ship must be in orbit to be able to extract and must have mining equipments installed that can
    extract goods, such as the `Gas Siphon` mount for gas-based goods or `Mining Laser` mount for ore-
    based goods.

    The survey property is now deprecated. See the `extract/survey` endpoint for more details.

    Args:
        ship_symbol (str):
        json_body (ExtractResourcesJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExtractResourcesResponse201
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
    json_body: ExtractResourcesJsonBody,
) -> Response[ExtractResourcesResponse201]:
    """Extract Resources

     Extract resources from a waypoint that can be extracted, such as asteroid fields, into your ship.
    Send an optional survey as the payload to target specific yields.

    The ship must be in orbit to be able to extract and must have mining equipments installed that can
    extract goods, such as the `Gas Siphon` mount for gas-based goods or `Mining Laser` mount for ore-
    based goods.

    The survey property is now deprecated. See the `extract/survey` endpoint for more details.

    Args:
        ship_symbol (str):
        json_body (ExtractResourcesJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExtractResourcesResponse201]
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
    json_body: ExtractResourcesJsonBody,
) -> Optional[ExtractResourcesResponse201]:
    """Extract Resources

     Extract resources from a waypoint that can be extracted, such as asteroid fields, into your ship.
    Send an optional survey as the payload to target specific yields.

    The ship must be in orbit to be able to extract and must have mining equipments installed that can
    extract goods, such as the `Gas Siphon` mount for gas-based goods or `Mining Laser` mount for ore-
    based goods.

    The survey property is now deprecated. See the `extract/survey` endpoint for more details.

    Args:
        ship_symbol (str):
        json_body (ExtractResourcesJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExtractResourcesResponse201
    """

    return (
        await asyncio_detailed(
            ship_symbol=ship_symbol,
            client=client,
            json_body=json_body,
        )
    ).parsed
