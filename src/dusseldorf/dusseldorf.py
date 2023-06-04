"""Asynchronous Python client providing Open Data information of Dusseldorf."""
from __future__ import annotations

import asyncio
import socket
from dataclasses import dataclass
from importlib import metadata
from typing import Any, cast

import async_timeout
from aiohttp import ClientError, ClientSession, hdrs
from yarl import URL

from .exceptions import ODPDusseldorfConnectionError, ODPDusseldorfError
from .models import DisabledParking, Garage, ParkAndRide


@dataclass
class ODPDusseldorf:
    """Main class for handling data fetchting from Open Data Platform of Dusseldorf."""

    request_timeout: float = 10.0
    session: ClientSession | None = None

    _close_session: bool = False

    async def _request(
        self,
        uri: str,
        *,
        method: str = hdrs.METH_GET,
        params: dict[str, Any] | None = None,
    ) -> Any:
        """Handle a request to the Open Data Platform API of Dusseldorf.

        Args:
        ----
            uri: Request URI, without '/', for example, 'status'
            method: HTTP method to use, for example, 'GET'
            params: Extra options to improve or limit the response.

        Returns:
        -------
            A Python dictionary (text) with the response from
            the Open Data Platform API of Dusseldorf.

        Raises:
        ------
            ODPDusseldorfConnectionError: Timeout occurred while
                connecting to the Open Data Platform API.
            ODPDusseldorfError: If the data is not valid.
        """
        version = metadata.version(__package__)
        url = URL.build(
            scheme="https",
            host="opendata.duesseldorf.de",
            path="/api/action/datastore/",
        ).join(URL(uri))

        headers = {
            "Accept": "application/json",
            "User-Agent": f"PythonODPDusseldorf/{version}",
        }

        if self.session is None:
            self.session = ClientSession()
            self._close_session = True

        try:
            async with async_timeout.timeout(self.request_timeout):
                response = await self.session.request(
                    method,
                    url,
                    params=params,
                    headers=headers,
                    ssl=True,
                )
                response.raise_for_status()
        except asyncio.TimeoutError as exception:
            msg = "Timeout occurred while connecting to the Open Data Platform API."
            raise ODPDusseldorfConnectionError(
                msg,
            ) from exception
        except (ClientError, socket.gaierror) as exception:
            msg = "Error occurred while communicating with Open Data Platform API."
            raise ODPDusseldorfConnectionError(
                msg,
            ) from exception

        content_type = response.headers.get("Content-Type", "")
        if "application/json" not in content_type:
            text = await response.text()
            msg = "Unexpected content type response from the Open Data Platform API"
            raise ODPDusseldorfError(
                msg,
                {"Content-Type": content_type, "Response": text},
            )

        return cast(dict[str, Any], await response.json())

    async def disabled_parkings(self, limit: int = 10) -> list[DisabledParking]:
        """Get list of disabled parkings.

        Args:
        ----
            limit: Maximum number of disabled parkings to return.

        Returns:
        -------
            A list of disabled parking objects.
        """
        results: list[DisabledParking] = []
        locations = await self._request(
            "search.json",
            params={
                "resource_id": "995914c7-4275-49c4-8441-426722336c3a",
                "limit": limit,
            },
        )
        for item in locations["result"]["records"]:
            results.append(DisabledParking.from_dict(item))
        return results

    async def garages(self, limit: int = 10) -> list[Garage]:
        """Get list of garages.

        Args:
        ----
            limit: Maximum number of garages to return.

        Returns:
        -------
            A list of garage objects.
        """
        results: list[Garage] = []
        locations = await self._request(
            "search.json",
            params={
                "resource_id": "53d63e70-0ed4-4175-9924-c45530d5bf29",
                "limit": limit,
            },
        )
        for item in locations["result"]["records"]:
            results.append(Garage.from_dict(item))
        return results

    async def park_and_rides(self, limit: int = 10) -> list[ParkAndRide]:
        """Get list of park and rides.

        Args:
        ----
            limit: Maximum number of park and rides to return.

        Returns:
        -------
            A list of park and ride objects.
        """
        results: list[ParkAndRide] = []
        locations = await self._request(
            "search.json",
            params={
                "resource_id": "1fd5b3f3-ea03-4922-9fae-3577fbc9f78a",
                "limit": limit,
            },
        )
        for item in locations["result"]["records"]:
            results.append(ParkAndRide.from_dict(item))
        return results

    async def close(self) -> None:
        """Close open client session."""
        if self.session and self._close_session:
            await self.session.close()

    async def __aenter__(self) -> ODPDusseldorf:
        """Async enter.

        Returns
        -------
            The Open Data Platform Dusseldorf object.
        """
        return self

    async def __aexit__(self, *_exc_info: Any) -> None:
        """Async exit.

        Args:
        ----
            _exc_info: Exec type.
        """
        await self.close()
