"""Test the models."""

from __future__ import annotations

from datetime import datetime

from aresponses import ResponsesMockServer

from dusseldorf import DisabledParking, Garage, ODPDusseldorf, ParkAndRide

from . import load_fixtures


async def test_all_garages(
    aresponses: ResponsesMockServer, odp_dusseldorf_client: ODPDusseldorf
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
    assert spaces is not None
    for item in spaces:
        assert isinstance(item, Garage)
        assert isinstance(item.entry_id, int)
        assert item.entry_id is not None
        assert isinstance(item.name, str)
        assert isinstance(item.longitude, float)
        assert isinstance(item.latitude, float)


async def test_all_park_and_rides(
    aresponses: ResponsesMockServer, odp_dusseldorf_client: ODPDusseldorf
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
    assert spaces is not None
    for item in spaces:
        assert isinstance(item, ParkAndRide)
        assert isinstance(item.entry_id, int)
        assert item.entry_id is not None
        assert isinstance(item.name, str)
        assert item.district is not None
        assert item.neighbourhood is not None
        assert isinstance(item.longitude, float)
        assert isinstance(item.latitude, float)


async def test_all_disabled_parkings(
    aresponses: ResponsesMockServer, odp_dusseldorf_client: ODPDusseldorf
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
    assert spaces is not None
    for item in spaces:
        assert isinstance(item, DisabledParking)
        assert isinstance(item.entry_id, str)
        assert item.entry_id is not None
        assert item.number is not None
        assert isinstance(item.longitude, float)
        assert isinstance(item.latitude, float)
        assert isinstance(item.last_update, datetime)
