# pylint: disable=W0621
"""Asynchronous Python client providing Open Data information of Dusseldorf."""

import asyncio

from dusseldorf import ODPDusseldorf


async def main() -> None:
    """Show example on using the Dusseldorf API client for park and rides."""
    async with ODPDusseldorf() as client:
        park_and_rides = await client.park_and_rides(limit=10)

        count: int = len(park_and_rides)
        for item in park_and_rides:
            print(item)

        print("__________________________")
        print(f"Total locations found: {count}")


if __name__ == "__main__":
    asyncio.run(main())
