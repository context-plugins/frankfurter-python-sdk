from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ServiceUnavailable(SdkBaseModel):
    message: Optional[str] = UNSET


class ServiceUnavailableDict(TypedDict):
    message: NotRequired[str]
