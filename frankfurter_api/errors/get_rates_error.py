from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.not_found1 import NotFound1
from ..models.service_unavailable1 import ServiceUnavailable1
from ..models.unprocessable_entity1 import UnprocessableEntity1

GetRatesErrorBody: TypeAlias = NotFound1 | UnprocessableEntity1 | ServiceUnavailable1 | RawError


@dataclass(frozen=True, slots=True)
class _GetRatesError:
    def map(self, status_code: int, content: bytes) -> GetRatesErrorBody:
        match status_code:
            case 404:
                return decode_json[NotFound1](content)
            case 422:
                return decode_json[UnprocessableEntity1](content)
            case 503:
                return decode_json[ServiceUnavailable1](content)
            case _:
                return RawError(status_code, content)


get_rates_error_mapper: Final[ErrorMapper[GetRatesErrorBody]] = _GetRatesError()
