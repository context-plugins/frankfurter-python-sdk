from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UnprocessableEntity(SdkBaseModel):
    message: Optional[str] = UNSET


class UnprocessableEntityDict(TypedDict):
    message: NotRequired[str]
