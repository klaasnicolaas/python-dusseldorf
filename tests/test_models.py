"""Test the models."""

from __future__ import annotations

from typing import TYPE_CHECKING

from aresponses import ResponsesMockServer
from syrupy.assertion import SnapshotAssertion

from . import load_fixtures

if TYPE_CHECKING:
    from dusseldorf import DisabledParking, Garage, ODPDusseldorf, ParkAndRide


async def test_all_garages(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    odp_dusseldorf_client: ODPDusseldorf,
) -> None:
    """Test all garages function."""
    aresponses.add(
        "opendata.duesseldorf.de",
        "/api/action/datastore/search.json",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("garages.json"),
        ),
    )
    spaces: list[Garage] = await odp_dusseldorf_client.garages()
    assert spaces == snapshot


async def test_all_park_and_rides(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    odp_dusseldorf_client: ODPDusseldorf,
) -> None:
    """Test park and ride spaces function."""
    aresponses.add(
        "opendata.duesseldorf.de",
        "/api/action/datastore/search.json",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("park_and_rides.json"),
        ),
    )
    spaces: list[ParkAndRide] = await odp_dusseldorf_client.park_and_rides()
    assert spaces == snapshot


async def test_all_disabled_parkings(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    odp_dusseldorf_client: ODPDusseldorf,
) -> None:
    """Test park and ride spaces function."""
    aresponses.add(
        "maps.duesseldorf.de",
        "/services/verkehr/wfs",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("disabled_parkings.json"),
        ),
    )
    spaces: list[DisabledParking] = await odp_dusseldorf_client.disabled_parkings()
    assert spaces == snapshot
