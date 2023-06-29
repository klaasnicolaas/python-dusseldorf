<!-- Banner -->
![alt Banner of the ODP Dusseldorf package](https://raw.githubusercontent.com/klaasnicolaas/python-dusseldorf/main/assets/header_dusseldorf-min.png)

<!-- PROJECT SHIELDS -->
[![GitHub Release][releases-shield]][releases]
[![Python Versions][python-versions-shield]][pypi]
![Project Stage][project-stage-shield]
![Project Maintenance][maintenance-shield]
[![License][license-shield]](LICENSE)

[![GitHub Activity][commits-shield]][commits-url]
[![PyPi Downloads][downloads-shield]][downloads-url]
[![GitHub Last Commit][last-commit-shield]][commits-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

[![Code Quality][code-quality-shield]][code-quality]
[![Build Status][build-shield]][build-url]
[![Typing Status][typing-shield]][typing-url]

[![Maintainability][maintainability-shield]][maintainability-url]
[![Code Coverage][codecov-shield]][codecov-url]

Asynchronous Python client for the open datasets of Dusseldorf (Germany).

## About

A python package with which you can retrieve data from the Open Data Platform of Dusseldorf via [their API][api]. This package was initially created to only retrieve parking data from the API, but the code base is made in such a way that it is easy to extend for other datasets from the same platform.

## Installation

```bash
pip install dusseldorf
```

## Datasets

You can read the following datasets with this package:

- [Disabled parking spaces / allgemeinen Behindertenparkplätze][disabled_parking] (315)
- [Park and rides locations / Park + Ride Anlagen][park_and_rides] (35)
- [Garage locations / Parkhäuser][garages] (55)

There are a number of parameters you can set to retrieve the data:

- **limit** (default: 10) - How many results you want to retrieve.

<details>
    <summary>Click here to get more details</summary>

### Disabled parking spaces

| Variable | Type | Description |
| :------- | :--- | :---------- |
| `entry_id` | string | The ID of the parking spot |
| `number` | integer | The number of parking spots on this location |
| `address` | string | The address of the parking spot |
| `district` | string | The district location of the parking spot |
| `time_limit` | string | Some locations have window times where the location is only specific for disabled parking, outside these times everyone is allowed to park there |
| `note` | string | Some locations have a note about the parking spot |
| `longitude` | float | The longitude of the parking spot |
| `latitude` | float | The latitude of the parking spot |
| `last_update` | datetime | The last time the data was updated |

### Park and Rides

| Variable | Type | Description |
| :------- | :--- | :---------- |
| `entry_id` | integer | The ID of the park and ride |
| `name` | string | The name of the park and ride |
| `address` | string | The address of the park and ride |
| `district` | integer | The district number of the park and ride |
| `neighbourhood` | string | The neighbourhood of the park and ride |
| `public_transport` | string | The public transport lines that is nearby |
| `longitude` | float | The longitude of the park and ride |
| `latitude` | float | The latitude of the park and ride |

### Garages

| Variable | Type | Description |
| :------- | :--- | :---------- |
| `entry_id` | integer | The ID of the garage |
| `name` | string | The name of the garage |
| `address` | string | The address of the garage |
| `location` | string | In which postcode area the garage is located |
| `longitude` | float | The longitude of the garage |
| `latitude` | float | The latitude of the garage |

</details>

## Example

```python
import asyncio

from dusseldorf import ODPDusseldorf


async def main() -> None:
    """Show example on using the Dusseldorf API client."""
    async with ODPDusseldorf() as client:
        disabled_parkings = await client.disabled_parkings()
        park_and_rides = await client.park_and_rides()
        garages = await client.garages()

        print(disabled_parkings)
        print(park_and_rides)
        print(garages)


if __name__ == "__main__":
    asyncio.run(main())
```

## Use cases

[NIPKaart.nl][nipkaart]

A website that provides insight into where disabled parking spaces are, based on
data from users and municipalities. Operates mainly in the Netherlands, but also
has plans to process data from abroad.

## Contributing

This is an active open-source project. We are always open to people who want to
use the code or contribute to it.

We've set up a separate document for our
[contribution guidelines](CONTRIBUTING.md).

Thank you for being involved! :heart_eyes:

## Setting up development environment

This Python project is fully managed using the [Poetry][poetry] dependency
manager.

You need at least:

- Python 3.9+
- [Poetry][poetry-install]

Install all packages, including all development requirements:

```bash
poetry install
```

Poetry creates by default an virtual environment where it installs all
necessary pip packages, to enter or exit the venv run the following commands:

```bash
poetry shell
exit
```

Setup the pre-commit check, you must run this inside the virtual environment:

```bash
pre-commit install
```

*Now you're all set to get started!*

As this repository uses the [pre-commit][pre-commit] framework, all changes
are linted and tested with each commit. You can run all checks and tests
manually, using the following command:

```bash
poetry run pre-commit run --all-files
```

To run just the Python tests:

```bash
poetry run pytest
```

## License

MIT License

Copyright (c) 2022-2023 Klaas Schoute

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[api]: https://opendata.duesseldorf.de/
[nipkaart]: https://www.nipkaart.nl

[disabled_parking]: https://opendata.duesseldorf.de/dataset/allgemeine-behindertenparkpl%C3%A4tze-d%C3%BCsseldorf
[park_and_rides]: https://opendata.duesseldorf.de/dataset/park-and-ride-anlagen-d%C3%BCsseldorf
[garages]: https://opendata.duesseldorf.de/dataset/parkh%C3%A4user-d%C3%BCsseldorf

<!-- MARKDOWN LINKS & IMAGES -->
[build-shield]: https://github.com/klaasnicolaas/python-dusseldorf/actions/workflows/tests.yaml/badge.svg
[build-url]: https://github.com/klaasnicolaas/python-dusseldorf/actions/workflows/tests.yaml
[code-quality-shield]: https://github.com/klaasnicolaas/python-dusseldorf/actions/workflows/codeql.yaml/badge.svg
[code-quality]: https://github.com/klaasnicolaas/python-dusseldorf/actions/workflows/codeql.yaml
[commits-shield]: https://img.shields.io/github/commit-activity/y/klaasnicolaas/python-dusseldorf.svg
[commits-url]: https://github.com/klaasnicolaas/python-dusseldorf/commits/main
[codecov-shield]: https://codecov.io/gh/klaasnicolaas/python-dusseldorf/branch/main/graph/badge.svg?token=3eJrHm0kV5
[codecov-url]: https://codecov.io/gh/klaasnicolaas/python-dusseldorf
[downloads-shield]: https://img.shields.io/pypi/dm/dusseldorf
[downloads-url]: https://pypistats.org/packages/dusseldorf
[issues-shield]: https://img.shields.io/github/issues/klaasnicolaas/python-dusseldorf.svg
[issues-url]: https://github.com/klaasnicolaas/python-dusseldorf/issues
[license-shield]: https://img.shields.io/github/license/klaasnicolaas/python-dusseldorf.svg
[last-commit-shield]: https://img.shields.io/github/last-commit/klaasnicolaas/python-dusseldorf.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2023.svg
[maintainability-shield]: https://api.codeclimate.com/v1/badges/516ae9d66f0766a671d0/maintainability
[maintainability-url]: https://codeclimate.com/github/klaasnicolaas/python-dusseldorf/maintainability
[project-stage-shield]: https://img.shields.io/badge/project%20stage-experimental-yellow.svg
[pypi]: https://pypi.org/project/dusseldorf/
[python-versions-shield]: https://img.shields.io/pypi/pyversions/dusseldorf
[typing-shield]: https://github.com/klaasnicolaas/python-dusseldorf/actions/workflows/typing.yaml/badge.svg
[typing-url]: https://github.com/klaasnicolaas/python-dusseldorf/actions/workflows/typing.yaml
[releases-shield]: https://img.shields.io/github/release/klaasnicolaas/python-dusseldorf.svg
[releases]: https://github.com/klaasnicolaas/python-dusseldorf/releases
[stars-shield]: https://img.shields.io/github/stars/klaasnicolaas/python-dusseldorf.svg
[stars-url]: https://github.com/klaasnicolaas/python-dusseldorf/stargazers

[poetry-install]: https://python-poetry.org/docs/#installation
[poetry]: https://python-poetry.org
[pre-commit]: https://pre-commit.com
