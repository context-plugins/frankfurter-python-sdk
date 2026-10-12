from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.not_found1 import NotFound1

GetCurrencyErrorBody: TypeAlias = NotFound1 | RawError


@dataclass(frozen=True, slots=True)
class _GetCurrencyError:
    def map(self, status_code: int, content: bytes) -> GetCurrencyErrorBody:
        match status_code:
            case 404:
                return decode_json[NotFound1](content)
            case _:
                return RawError(status_code, content)


get_currency_error_mapper: Final[ErrorMapper[GetCurrencyErrorBody]] = _GetCurrencyError()
