from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.not_found1 import NotFound1
from ..models.service_unavailable1 import ServiceUnavailable1
from ..models.unprocessable_entity1 import UnprocessableEntity1

GetRateErrorBody: TypeAlias = NotFound1 | UnprocessableEntity1 | ServiceUnavailable1 | RawError


@dataclass(frozen=True, slots=True)
class _GetRateError:
    def map(self, response: HttpResponse) -> GetRateErrorBody:
        match response.status_code:
            case 404:
                return decode_json[NotFound1](response)
            case 422:
                return decode_json[UnprocessableEntity1](response)
            case 503:
                return decode_json[ServiceUnavailable1](response)
            case _:
                return RawError(response)


get_rate_error_mapper: Final[ErrorMapper[GetRateErrorBody]] = _GetRateError()
