from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Peg(SdkBaseModel):
    """Peg metadata, present only for pegged currencies"""

    base: Optional[str] = UNSET
    rate: Optional[float] = UNSET
    authority: Optional[str] = UNSET
    source: Optional[str] = UNSET


class PegDict(TypedDict):
    base: NotRequired[str]
    rate: NotRequired[float]
    authority: NotRequired[str]
    source: NotRequired[str]
