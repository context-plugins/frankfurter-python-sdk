from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PublishCadence(str, Enum):
    """How often the provider publishes rates. Determines the unit of publishes_missed: a count of days, ISO weeks, or
    calendar months. Null for historical-only providers with no scheduled cadence."""

    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"

    __str__ = str.__str__


PublishCadenceOrStr: TypeAlias = Annotated[PublishCadence | str, open_enum_validator(PublishCadence)]
