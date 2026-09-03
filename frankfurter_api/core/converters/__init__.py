"""Wire-format converters a generated model names in its annotations.

A datetime/date field names one of the four ``Annotated`` aliases -- ``RFC3339DateTime``,
``RFC1123DateTime``, ``UnixSecondsDateTime``, ``Date`` -- and an open enum field pairs its type with
:func:`open_enum_validator`. The bare ``DateTimeConverter`` pairs that build the aliases stay
internal to ``date_time``."""

from .date_time import Date, RFC1123DateTime, RFC3339DateTime, UnixSecondsDateTime
from .open_enum import open_enum_validator

__all__ = [
    # Wire-format datetime/date aliases
    "Date",
    "RFC3339DateTime",
    "RFC1123DateTime",
    "UnixSecondsDateTime",
    # Open enums
    "open_enum_validator",
]
