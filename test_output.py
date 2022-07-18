# pylint: disable=W0621
"""Asynchronous Python client providing Open Data information of Dusseldorf."""

import asyncio

from dusseldorf import ODPDusseldorf


async def main() -> None:
    """Show example on using the Dusseldorf API client."""
    async with ODPDusseldorf() as client:
        disabled_parkings = await client.disabled_parkings()
        garages = await client.garages()
        park_and_rides = await client.park_and_rides()

        print(disabled_parkings)
        print(garages)

        count: int
        for index, item in enumerate(park_and_rides, 1):
            count = index
            print(item)
        print(f"{count} locations found")


if __name__ == "__main__":
    asyncio.run(main())
