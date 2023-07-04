# pylint: disable=W0621
"""Asynchronous Python client providing Open Data information of Dusseldorf."""

import asyncio

from dusseldorf import ODPDusseldorf


async def main() -> None:
    """Show example on using the Dusseldorf API client for garages."""
    async with ODPDusseldorf() as client:
        garages = await client.garages(limit=10)

        count: int = len(garages)
        for item in garages:
            print(item)

        print("__________________________")
        print(f"Total locations found: {count}")


if __name__ == "__main__":
    asyncio.run(main())
