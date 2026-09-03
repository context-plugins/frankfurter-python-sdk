from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .base_client import DEFAULT_TIMEOUT, BaseFrankfurterApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiResult,
    BaseRawResponse,
    Date,
    HttpClient,
    HttpxClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    json_decoder,
    param,
    raw_error_response,
)
from .errors.get_currency_error import GetCurrencyErrorBody, get_currency_error_mapper
from .errors.get_rate_error import GetRateErrorBody, get_rate_error_mapper
from .errors.get_rates_error import GetRatesErrorBody, get_rates_error_mapper
from .models.currency import Currency
from .models.currency_detail import CurrencyDetail
from .models.enums.expand import ExpandOrStr
from .models.enums.group import GroupOrStr
from .models.enums.scope import ScopeOrStr
from .models.provider import Provider
from .models.rate import Rate
from .server.server import Server


class FrankfurterApiClient(BaseFrankfurterApiClient[RawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_http_client: HttpClient | None = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout),
            global_headers=[
                param[str]("User-Agent", "FrankfurterApiClient/2.1.1 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "2.1.1"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )

    @cached_property
    def with_raw_response(self) -> ApiWithRawResponse:
        return ApiWithRawResponse(self._raw_client, self._server)

    def get_currencies(
        self,
        *,
        scope: ScopeOrStr | None = None,
        providers: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Currency]:
        """Returns available currencies with their names and date ranges. By default, only active currencies are
        included.

        Args:
            scope: Set to 'all' to include legacy currencies
            providers: Comma-separated list of data providers to include
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Available currencies

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.get_currencies(
            scope=scope, providers=providers, request_options=request_options
        ).unwrap()

    def get_currency(self, code: str, *, request_options: RequestOptionsOrDict | None = None) -> CurrencyDetail:
        """Returns details for a single currency, including provider information or peg metadata.

        Args:
            code: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Currency details

        Raises:
            ApiError: No data found ``error`` is ``NotFound1 | RawError``."""
        return self.with_raw_response.get_currency(code, request_options=request_options).unwrap()

    def get_providers(self, *, request_options: RequestOptionsOrDict | None = None) -> list[Provider]:
        """Returns available exchange rate data providers with their base currency.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Available providers

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.get_providers(request_options=request_options).unwrap()

    def get_rate(
        self,
        base: str,
        quote: str,
        *,
        date: Date | None = None,
        providers: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Rate:
        """Returns the blended exchange rate for a single currency pair. Without a date param, returns the latest rate.
        A same-currency pair returns the identity rate of 1.

        Args:
            base: Value sent with the request.
            quote: Value sent with the request.
            date: Specific date (YYYY-MM-DD). Cannot be combined with from/to.
            providers: Comma-separated list of data providers to include
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Exchange rate

        Raises:
            ApiError: Invalid request No data found The request deadline expired before the response could be computed.
                Retry with a narrower request: filter with quotes, aggregate with group, or split the range into shorter
                requests. ``error`` is ``NotFound1 | UnprocessableEntity1 | ServiceUnavailable1 | RawError``."""
        return self.with_raw_response.get_rate(
            base, quote, date=date, providers=providers, request_options=request_options
        ).unwrap()

    def get_rates(
        self,
        *,
        date: Date | None = None,
        from_: Date | None = None,
        to: Date | None = None,
        base: str | None = "EUR",
        quotes: str | None = None,
        providers: str | None = None,
        group: GroupOrStr | None = None,
        expand: ExpandOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Rate]:
        """Returns exchange rates blended across providers. Without date params, returns the latest rates. Each record
        is a single currency pair. The response includes an identity record for the base currency (base equals quote,
        rate 1), subject to the quotes filter like any other record. Daily date ranges of any length are served,
        including full history. Limit: requests using ``providers`` or ``expand=providers`` recompute the blend per
        date, so at daily granularity they return 422 for ranges longer than 5 years. With ``providers`` naming at most
        5 providers, a ``quotes`` list of at most 5 currencies lifts the cap; without ``providers``,
        ``expand=providers`` ranges compute every currency regardless of ``quotes``, so aggregate with ``group=week`` or
        ``group=month``, add ``providers``, or split the range into shorter requests.

        Args:
            date: Specific date (YYYY-MM-DD). Cannot be combined with from/to.
            from_: Start of date range (YYYY-MM-DD)
            to: End of date range (YYYY-MM-DD). Defaults to today.
            base: Base currency (default: EUR)
            quotes: Comma-separated list of quote currencies to include
            providers: Comma-separated list of data providers to include
            group: Downsample rates by time period. Only applies to date ranges.
            expand: Comma-separated list of optional fields to include per record. Currently supports ``providers``,
                which adds an array of ``{ key, date, rate }`` objects per record showing each provider's individual
                observation date and rate. Outliers excluded from the blend (and providers whose rate was overridden by
                a currency peg) are flagged with ``excluded: true``. The field is omitted on synthesized peg rows where
                no provider published the quote. In CSV output, the ``providers`` column is encoded as ``KEY:RATE``
                pairs joined by ``|``, with a trailing ``*`` on excluded entries (e.g. ``ECB:0.92|FED:1.50*``).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Exchange rates

        Raises:
            ApiError: Invalid request No data found The request deadline expired before the response could be computed.
                Retry with a narrower request: filter with quotes, aggregate with group, or split the range into shorter
                requests. ``error`` is ``NotFound1 | UnprocessableEntity1 | ServiceUnavailable1 | RawError``."""
        return self.with_raw_response.get_rates(
            date=date,
            from_=from_,
            to=to,
            base=base,
            quotes=quotes,
            providers=providers,
            group=group,
            expand=expand,
            request_options=request_options,
        ).unwrap()

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


class ApiWithRawResponse(BaseRawResponse[RawClient, Server]):
    def get_currencies(
        self,
        *,
        scope: ScopeOrStr | None = None,
        providers: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Currency], RawError]:
        """Returns available currencies with their names and date ranges. By default, only active currencies are
        included.

        Args:
            scope: Set to 'all' to include legacy currencies
            providers: Comma-separated list of data providers to include
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/currencies"),
            query_params=[param[ScopeOrStr | None]("scope", scope), param[str | None]("providers", providers)],
            decoder=json_decoder[list[Currency]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_currency(
        self, code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CurrencyDetail, GetCurrencyErrorBody]:
        """Returns details for a single currency, including provider information or peg metadata.

        Args:
            code: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/currency/{code}"),
            path_params=[param[str]("code", code)],
            decoder=json_decoder[CurrencyDetail],
            error_mapper=get_currency_error_mapper,
            request_options=request_options,
        )

    def get_providers(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Provider], RawError]:
        """Returns available exchange rate data providers with their base currency.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/providers"),
            decoder=json_decoder[list[Provider]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_rate(
        self,
        base: str,
        quote: str,
        *,
        date: Date | None = None,
        providers: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Rate, GetRateErrorBody]:
        """Returns the blended exchange rate for a single currency pair. Without a date param, returns the latest rate.
        A same-currency pair returns the identity rate of 1.

        Args:
            base: Value sent with the request.
            quote: Value sent with the request.
            date: Specific date (YYYY-MM-DD). Cannot be combined with from/to.
            providers: Comma-separated list of data providers to include
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/rate/{base}/{quote}"),
            path_params=[param[str]("base", base), param[str]("quote", quote)],
            query_params=[param[Date | None]("date", date), param[str | None]("providers", providers)],
            decoder=json_decoder[Rate],
            error_mapper=get_rate_error_mapper,
            request_options=request_options,
        )

    def get_rates(
        self,
        *,
        date: Date | None = None,
        from_: Date | None = None,
        to: Date | None = None,
        base: str | None = "EUR",
        quotes: str | None = None,
        providers: str | None = None,
        group: GroupOrStr | None = None,
        expand: ExpandOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Rate], GetRatesErrorBody]:
        """Returns exchange rates blended across providers. Without date params, returns the latest rates. Each record
        is a single currency pair. The response includes an identity record for the base currency (base equals quote,
        rate 1), subject to the quotes filter like any other record. Daily date ranges of any length are served,
        including full history. Limit: requests using ``providers`` or ``expand=providers`` recompute the blend per
        date, so at daily granularity they return 422 for ranges longer than 5 years. With ``providers`` naming at most
        5 providers, a ``quotes`` list of at most 5 currencies lifts the cap; without ``providers``,
        ``expand=providers`` ranges compute every currency regardless of ``quotes``, so aggregate with ``group=week`` or
        ``group=month``, add ``providers``, or split the range into shorter requests.

        Args:
            date: Specific date (YYYY-MM-DD). Cannot be combined with from/to.
            from_: Start of date range (YYYY-MM-DD)
            to: End of date range (YYYY-MM-DD). Defaults to today.
            base: Base currency (default: EUR)
            quotes: Comma-separated list of quote currencies to include
            providers: Comma-separated list of data providers to include
            group: Downsample rates by time period. Only applies to date ranges.
            expand: Comma-separated list of optional fields to include per record. Currently supports ``providers``,
                which adds an array of ``{ key, date, rate }`` objects per record showing each provider's individual
                observation date and rate. Outliers excluded from the blend (and providers whose rate was overridden by
                a currency peg) are flagged with ``excluded: true``. The field is omitted on synthesized peg rows where
                no provider published the quote. In CSV output, the ``providers`` column is encoded as ``KEY:RATE``
                pairs joined by ``|``, with a trailing ``*`` on excluded entries (e.g. ``ECB:0.92|FED:1.50*``).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/rates"),
            query_params=[
                param[Date | None]("date", date),
                param[Date | None]("from", from_),
                param[Date | None]("to", to),
                param[str | None]("base", base),
                param[str | None]("quotes", quotes),
                param[str | None]("providers", providers),
                param[GroupOrStr | None]("group", group),
                param[ExpandOrStr | None]("expand", expand),
            ],
            decoder=json_decoder[list[Rate]],
            error_mapper=get_rates_error_mapper,
            request_options=request_options,
        )


Client = FrankfurterApiClient
