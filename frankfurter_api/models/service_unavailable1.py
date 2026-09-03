from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ServiceUnavailable1(SdkBaseModel):
    message: Optional[str] = UNSET


class ServiceUnavailable1Dict(TypedDict):
    message: NotRequired[str]
