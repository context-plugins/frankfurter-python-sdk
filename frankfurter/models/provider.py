from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, OptionalNullable, SdkBaseModel
from .enums.publish_cadence import PublishCadenceOrStr


class Provider(SdkBaseModel):
    key: str
    """Provider identifier"""

    name: str
    """Full provider name"""

    country_code: OptionalNullable[str] = UNSET
    """ISO 3166-1 alpha-2 country code"""

    rate_type: OptionalNullable[str] = UNSET
    """Official rate type as used by the source"""

    pivot_currency: OptionalNullable[str] = UNSET
    """Base currency for published rates"""

    data_url: OptionalNullable[str] = UNSET
    """Link to the data source"""

    terms_url: OptionalNullable[str] = UNSET
    """Link to terms of use"""

    start_date: OptionalNullable[Date] = UNSET
    """Earliest available date"""

    end_date: OptionalNullable[Date] = UNSET
    """Latest available date"""

    publish_cadence: OptionalNullable[PublishCadenceOrStr] = UNSET
    """How often the provider publishes rates. Determines the unit of publishes_missed: a count of days, ISO weeks, or
    calendar months. Null for historical-only providers with no scheduled cadence."""

    publishes_missed: OptionalNullable[int] = UNSET
    """Number of expected publishes missed since end_date, in units of publish_cadence. For daily providers, counts
    scheduled publish days strictly between end_date and today. For weekly and monthly providers, counts ISO weeks or
    calendar months between the latest imported bucket and the bucket whose publish window has already started. Null
    when the provider has no scheduled cadence or no imported data."""

    currencies: list[str]
    """Currency codes covered by this provider"""


class ProviderDict(TypedDict):
    key: str
    name: str
    country_code: NotRequired[str | None]
    rate_type: NotRequired[str | None]
    pivot_currency: NotRequired[str | None]
    data_url: NotRequired[str | None]
    terms_url: NotRequired[str | None]
    start_date: NotRequired[Date | None]
    end_date: NotRequired[Date | None]
    publish_cadence: NotRequired[PublishCadenceOrStr | None]
    publishes_missed: NotRequired[int | None]
    currencies: list[str]
