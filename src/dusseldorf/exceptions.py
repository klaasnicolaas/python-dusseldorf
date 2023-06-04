"""Asynchronous Python client providing Open Data information of Dusseldorf."""


class ODPDusseldorfError(Exception):
    """Generic Open Data Platform Dusseldorf exception."""


class ODPDusseldorfConnectionError(ODPDusseldorfError):
    """Open Data Platform Dusseldorf - connection error."""
