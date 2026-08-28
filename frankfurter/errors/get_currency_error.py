from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.not_found1 import NotFound1

GetCurrencyErrorBody: TypeAlias = NotFound1 | RawError


@dataclass(frozen=True, slots=True)
class _GetCurrencyError:
    def map(self, response: HttpResponse) -> GetCurrencyErrorBody:
        match response.status_code:
            case 404:
                return decode_json[NotFound1](response)
            case _:
                return RawError(response)


get_currency_error_mapper: Final[ErrorMapper[GetCurrencyErrorBody]] = _GetCurrencyError()
