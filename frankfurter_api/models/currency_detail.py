from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .peg import Peg, PegDict


class CurrencyDetail(SdkBaseModel):
    iso_code: str
    """ISO 4217 currency code"""

    iso_numeric: OptionalNullable[str] = UNSET
    """ISO 4217 numeric code"""

    name: str
    """Full currency name"""

    symbol: OptionalNullable[str] = UNSET
    """Currency symbol"""

    providers: Optional[list[str]] = UNSET
    """Provider keys that publish this currency"""

    peg: Optional[Peg] = UNSET
    """Peg metadata, present only for pegged currencies"""


class CurrencyDetailDict(TypedDict):
    iso_code: str
    iso_numeric: NotRequired[str | None]
    name: str
    symbol: NotRequired[str | None]
    providers: NotRequired[list[str]]
    peg: NotRequired[Peg | PegDict]
