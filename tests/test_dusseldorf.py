"""Basic tests for the Open Data Platform API of Dusseldorf."""

# pylint: disable=protected-access
import asyncio
from unittest.mock import patch

import pytest
from aiohttp import ClientError, ClientResponse, ClientSession
from aresponses import Response, ResponsesMockServer

from dusseldorf import ODPDusseldorf
from dusseldorf.exceptions import ODPDusseldorfConnectionError, ODPDusseldorfError

from . import load_fixtures


async def test_json_request(
    aresponses: ResponsesMockServer, odp_dusseldorf_client: ODPDusseldorf
) -> None:
    """Test JSON response is handled correctly."""
    aresponses.add(
        "opendata.duesseldorf.de",
        "/api/action/datastore/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("disabled_parkings.json"),
        ),
    )
    await odp_dusseldorf_client._request("test")
    await odp_dusseldorf_client.close()


async def test_internal_session(aresponses: ResponsesMockServer) -> None:
    """Test internal session is handled correctly."""
    aresponses.add(
        "opendata.duesseldorf.de",
        "/api/action/datastore/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("disabled_parkings.json"),
        ),
    )
    async with ODPDusseldorf() as client:
        await client._request("test")


async def test_timeout(aresponses: ResponsesMockServer) -> None:
    """Test request timeout from the Open Data Platform API of Dusseldorf."""

    # Faking a timeout by sleeping
    async def response_handler(_: ClientResponse) -> Response:
        await asyncio.sleep(0.2)
        return aresponses.Response(
            body="Goodmorning!",
            text=load_fixtures("disabled_parkings.json"),
        )

    aresponses.add(
        "opendata.duesseldorf.de",
        "/api/action/datastore/test",
        "GET",
        response_handler,
    )

    async with ClientSession() as session:
        client = ODPDusseldorf(
            session=session,
            request_timeout=0.1,
        )
        with pytest.raises(ODPDusseldorfConnectionError):
            assert await client._request("test")


async def test_content_type(
    aresponses: ResponsesMockServer, odp_dusseldorf_client: ODPDusseldorf
) -> None:
    """Test request content type error from Open Data Platform API of Dusseldorf."""
    aresponses.add(
        "opendata.duesseldorf.de",
        "/api/action/datastore/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "blabla/blabla"},
        ),
    )
    with pytest.raises(ODPDusseldorfError):
        assert await odp_dusseldorf_client._request("test")


async def test_client_error() -> None:
    """Test request client error from the Open Data Platform API of Dusseldorf."""
    async with ClientSession() as session:
        client = ODPDusseldorf(session=session)
        with (
            patch.object(
                session,
                "request",
                side_effect=ClientError,
            ),
            pytest.raises(ODPDusseldorfConnectionError),
        ):
            assert await client._request("test")
