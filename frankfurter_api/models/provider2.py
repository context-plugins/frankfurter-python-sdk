from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class Provider2(SdkBaseModel):
    key: str
    """Provider key"""

    date: Date
    """Provider observation date used for this entry"""

    rate: float
    """Provider's rate, rebased to the row's base"""

    excluded: Optional[bool] = UNSET
    """Present and true when this entry did not contribute to the blended rate"""


class Provider2Dict(TypedDict):
    key: str
    date: Date
    rate: float
    excluded: NotRequired[bool]
