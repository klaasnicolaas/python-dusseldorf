# pylint: disable=W0621
"""Asynchronous Python client providing Open Data information of Dusseldorf."""

import asyncio

from dusseldorf import ODPDusseldorf


async def main() -> None:
    """Show example on using the Dusseldorf API client for disabled parkings."""
    async with ODPDusseldorf() as client:
        disabled_parkings = await client.disabled_parkings(limit=10)

        count: int
        for index, item in enumerate(disabled_parkings, 1):
            count = index
            print(item)
        print(f"{count} locations found")


if __name__ == "__main__":
    asyncio.run(main())
