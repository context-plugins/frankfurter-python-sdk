from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .provider2 import Provider2, Provider2Dict


class Rate(SdkBaseModel):
    date: Date
    """The date of the rate"""

    base: str
    """Base currency code"""

    quote: str
    """Quote currency code"""

    rate: float
    """Exchange rate value"""

    providers: Optional[list[Provider2]] = UNSET
    """Per-provider rates for this pair. Present only when ``expand=providers`` is set. Each entry has the provider's
    observation date and published rate (rebased to the row's base). Entries with ``excluded: true`` did not contribute
    to the blended ``rate`` — either flagged as outliers by the consensus filter, or overridden by a currency peg.
    Omitted on synthesized peg rows where no provider published the quote."""


class RateDict(TypedDict):
    date: Date
    base: str
    quote: str
    rate: float
    providers: NotRequired[list[Provider2Dict]]
