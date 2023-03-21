"""Models for Open Data Platform of Dusseldorf."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class ParkAndRide:
    """Object representing a ParkAndRide."""

    entry_id: int
    name: str
    address: str
    district: int | None
    neighbourhood: str | None
    public_transport: str
    longitude: float
    latitude: float

    @classmethod
    def from_dict(cls: type[ParkAndRide], data: dict[str, Any]) -> ParkAndRide:
        """Return a ParkAndRide object from a dictionary.

        Args:
        ----
            data: The data from the API.

        Returns:
        -------
            A ParkAndRide object.
        """
        return cls(
            entry_id=int(data["entry_id"]),
            name=data["name"],
            address=set_address(
                data["strasse"],
                data["hausnummer"],
            ),
            district=data["stadtbezirk"] or None,
            neighbourhood=str(data["stadt"][11:]) or None,
            public_transport=data["nahverkehr"],
            longitude=float(data["longitude"]),
            latitude=float(data["latitude"]),
        )


@dataclass
class DisabledParking:
    """Object representing a DisabledParking."""

    entry_id: int
    name: str
    number: int
    address: str
    time_limit: str | None
    note: str | None
    longitude: float
    latitude: float

    @classmethod
    def from_dict(cls: type[DisabledParking], data: dict[str, Any]) -> DisabledParking:
        """Return a DisabledParking object from a dictionary.

        Args:
        ----
            data: The data from the API.

        Returns:
        -------
            A DisabledParking object.
        """
        return cls(
            entry_id=int(data["entry_id"]),
            name=data["name"],
            number=int(data["anzahl"]),
            address=set_address(
                data["strasse"],
                data["hausnr"],
            ),
            time_limit=data.get("zeitbegrenzung") or None,
            note=data.get("bemerkung") or None,
            longitude=float(data["longitude"]),
            latitude=float(data["latitude"]),
        )


@dataclass
class Garage:
    """Object representing a Garage."""

    entry_id: int
    name: str
    address: str
    location: str
    longitude: float
    latitude: float

    @classmethod
    def from_dict(cls: type[Garage], data: dict[str, Any]) -> Garage:
        """Return a Garage object from a dictionary.

        Args:
        ----
            data: The data from the API.

        Returns:
        -------
            A Garage object.
        """
        return cls(
            entry_id=int(data["entry_id"]),
            name=data["name"],
            address=data["adresse_zufahrt"],
            location=data["ort"],
            longitude=float(data["longitude"]),
            latitude=float(data["latitude"]),
        )


def set_address(street: str, number: str) -> str:
    """Set the address.

    Args:
    ----
        street: The street name.
        number: The house number.

    Returns:
    -------
        The address.
    """
    return f"{street} {number}"
