<!-- Generated file — do not edit; regenerated with the SDK. -->

# Client — operations

Accessor: `client` · Source: `frankfurter/client.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.get_currencies

- **Route**: `GET /currencies`
- **Signature**: `def get_currencies(*, scope: ScopeOrStr | None = None, providers: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `scope` — query · `providers` — query
- **Returns (parsed)**: `list[Currency]`
- **Returns (raw)**: `ApiResult[list[Currency], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ScopeOrStr` | `frankfurter/models/enums/scope.py` |
| `Currency` | `frankfurter/models/currency.py` |

### client.get_currency

- **Route**: `GET /currency/{code}`
- **Signature**: `def get_currency(code: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `code`
- **Params**: `code` — path
- **Returns (parsed)**: `CurrencyDetail`
- **Returns (raw)**: `ApiResult[CurrencyDetail, GetCurrencyErrorBody]`
- **Error**: `GetCurrencyErrorBody` — **Case A (typed)**
- **Error arms**: `NotFound1` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CurrencyDetail` | `frankfurter/models/currency_detail.py` |
| `GetCurrencyErrorBody` | `frankfurter/errors/get_currency_error.py` |
| `NotFound1` | `frankfurter/models/not_found1.py` |

### client.get_providers

- **Route**: `GET /providers`
- **Signature**: `def get_providers(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[Provider]`
- **Returns (raw)**: `ApiResult[list[Provider], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Provider` | `frankfurter/models/provider.py` |

### client.get_rate

- **Route**: `GET /rate/{base}/{quote}`
- **Signature**: `def get_rate(base: str, quote: str, *, date: Date | None = None, providers: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `base`, `quote`
- **Params**: `base` — path · `quote` — path · `date` — query · `providers` — query
- **Returns (parsed)**: `Rate`
- **Returns (raw)**: `ApiResult[Rate, GetRateErrorBody]`
- **Error**: `GetRateErrorBody` — **Case A (typed)**
- **Error arms**: `NotFound1` [404] · `UnprocessableEntity1` [422] · `ServiceUnavailable1` [503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Rate` | `frankfurter/models/rate.py` |
| `GetRateErrorBody` | `frankfurter/errors/get_rate_error.py` |
| `NotFound1` | `frankfurter/models/not_found1.py` |
| `UnprocessableEntity1` | `frankfurter/models/unprocessable_entity1.py` |
| `ServiceUnavailable1` | `frankfurter/models/service_unavailable1.py` |

### client.get_rates

- **Route**: `GET /rates`
- **Signature**: `def get_rates(*, date: Date | None = None, from_: Date | None = None, to: Date | None = None, base: str | None = "EUR", quotes: str | None = None, providers: str | None = None, group: GroupOrStr | None = None, expand: ExpandOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `date` — query · `from_` — query `from` · `to` — query · `base` — query · `quotes` — query · `providers` — query · `group` — query · `expand` — query
- **Returns (parsed)**: `list[Rate]`
- **Returns (raw)**: `ApiResult[list[Rate], GetRatesErrorBody]`
- **Error**: `GetRatesErrorBody` — **Case A (typed)**
- **Error arms**: `NotFound1` [404] · `UnprocessableEntity1` [422] · `ServiceUnavailable1` [503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GroupOrStr` | `frankfurter/models/enums/group.py` |
| `ExpandOrStr` | `frankfurter/models/enums/expand.py` |
| `Rate` | `frankfurter/models/rate.py` |
| `GetRatesErrorBody` | `frankfurter/errors/get_rates_error.py` |
| `NotFound1` | `frankfurter/models/not_found1.py` |
| `UnprocessableEntity1` | `frankfurter/models/unprocessable_entity1.py` |
| `ServiceUnavailable1` | `frankfurter/models/service_unavailable1.py` |

