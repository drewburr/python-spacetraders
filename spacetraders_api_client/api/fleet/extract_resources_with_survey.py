from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.extract_resources_with_survey_response_201 import (
    ExtractResourcesWithSurveyResponse201,
)
from ...models.survey import Survey
from ...types import Response


def _get_kwargs(
    ship_symbol: str,
    *,
    json_body: Survey,
) -> Dict[str, Any]:
    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/my/ships/{shipSymbol}/extract/survey".format(
            shipSymbol=ship_symbol,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ExtractResourcesWithSurveyResponse201]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = ExtractResourcesWithSurveyResponse201.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ExtractResourcesWithSurveyResponse201]:
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
    json_body: Survey,
) -> Response[ExtractResourcesWithSurveyResponse201]:
    """Extract Resources with Survey

     Use a survey when extracting resources from a waypoint. This endpoint requires a survey as the
    payload, which allows your ship to extract specific yields.

    Send the full survey object as the payload which will be validated according to the signature. If
    the signature is invalid, or any properties of the survey are changed, the request will fail.

    Args:
        ship_symbol (str):
        json_body (Survey): A resource survey of a waypoint, detailing a specific extraction
            location and the types of resources that can be found there.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExtractResourcesWithSurveyResponse201]
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
    json_body: Survey,
) -> Optional[ExtractResourcesWithSurveyResponse201]:
    """Extract Resources with Survey

     Use a survey when extracting resources from a waypoint. This endpoint requires a survey as the
    payload, which allows your ship to extract specific yields.

    Send the full survey object as the payload which will be validated according to the signature. If
    the signature is invalid, or any properties of the survey are changed, the request will fail.

    Args:
        ship_symbol (str):
        json_body (Survey): A resource survey of a waypoint, detailing a specific extraction
            location and the types of resources that can be found there.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExtractResourcesWithSurveyResponse201
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
    json_body: Survey,
) -> Response[ExtractResourcesWithSurveyResponse201]:
    """Extract Resources with Survey

     Use a survey when extracting resources from a waypoint. This endpoint requires a survey as the
    payload, which allows your ship to extract specific yields.

    Send the full survey object as the payload which will be validated according to the signature. If
    the signature is invalid, or any properties of the survey are changed, the request will fail.

    Args:
        ship_symbol (str):
        json_body (Survey): A resource survey of a waypoint, detailing a specific extraction
            location and the types of resources that can be found there.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExtractResourcesWithSurveyResponse201]
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
    json_body: Survey,
) -> Optional[ExtractResourcesWithSurveyResponse201]:
    """Extract Resources with Survey

     Use a survey when extracting resources from a waypoint. This endpoint requires a survey as the
    payload, which allows your ship to extract specific yields.

    Send the full survey object as the payload which will be validated according to the signature. If
    the signature is invalid, or any properties of the survey are changed, the request will fail.

    Args:
        ship_symbol (str):
        json_body (Survey): A resource survey of a waypoint, detailing a specific extraction
            location and the types of resources that can be found there.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExtractResourcesWithSurveyResponse201
    """

    return (
        await asyncio_detailed(
            ship_symbol=ship_symbol,
            client=client,
            json_body=json_body,
        )
    ).parsed
