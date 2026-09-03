from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, OptionalNullable, SdkBaseModel


class Currency(SdkBaseModel):
    iso_code: str
    """ISO 4217 currency code"""

    iso_numeric: OptionalNullable[str] = UNSET
    """ISO 4217 numeric code"""

    name: str
    """Full currency name"""

    symbol: OptionalNullable[str] = UNSET
    """Currency symbol"""

    start_date: OptionalNullable[Date] = UNSET
    """Earliest available date"""

    end_date: OptionalNullable[Date] = UNSET
    """Latest available date"""


class CurrencyDict(TypedDict):
    iso_code: str
    iso_numeric: NotRequired[str | None]
    name: str
    symbol: NotRequired[str | None]
    start_date: NotRequired[Date | None]
    end_date: NotRequired[Date | None]
