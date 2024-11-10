"""Fixture for the ODP Dusseldorf tests."""

from collections.abc import AsyncGenerator

import pytest
from aiohttp import ClientSession

from dusseldorf import ODPDusseldorf


@pytest.fixture(name="odp_dusseldorf_client")
async def client() -> AsyncGenerator[ODPDusseldorf, None]:
    """Return an ODP Dusseldorf client."""
    async with (
        ClientSession() as session,
        ODPDusseldorf(session=session) as odp_dusseldorf_client,
    ):
        yield odp_dusseldorf_client
