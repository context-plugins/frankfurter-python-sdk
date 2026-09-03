# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [FrankfurterApiClient](frankfurter_api/client.py)

<details>
<summary><code>def get_currencies(*, scope: ScopeOrStr | None = None, providers: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Currency], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns available currencies with their names and date ranges. By default, only active currencies are included.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.get_currencies()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Currency]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.get_currencies()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Currency]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>scope</code> | <code>[ScopeOrStr](frankfurter_api/models/enums/scope.py) \| None</code> | Set to 'all' to include legacy currencies<br>**Default**: <code>None</code> |
| <code>providers</code> | <code>str \| None</code> | Comma-separated list of data providers to include<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](frankfurter_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](frankfurter_api/core/results.py)&#91;list&#91;[Currency](frankfurter_api/models/currency.py)&#93;, [RawError](frankfurter_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Currency](frankfurter_api/models/currency.py)&#93;</code> -- Available currencies

**On `Failure`**: `error` is <code>[RawError](frankfurter_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_currency(code: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CurrencyDetail, GetCurrencyErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns details for a single currency, including provider information or peg metadata.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.get_currency(code)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CurrencyDetail
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCurrencyErrorBody
```

**Async**

```python
result = await async_client.with_raw_response.get_currency(code)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CurrencyDetail
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCurrencyErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>code</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](frankfurter_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](frankfurter_api/core/results.py)&#91;[CurrencyDetail](frankfurter_api/models/currency_detail.py), [GetCurrencyErrorBody](frankfurter_api/errors/get_currency_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CurrencyDetail](frankfurter_api/models/currency_detail.py)</code> -- Currency details

**On `Failure`**: `error` is <code>[GetCurrencyErrorBody](frankfurter_api/errors/get_currency_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[NotFound1](frankfurter_api/models/not_found1.py)</code> |
| anything unmapped | <code>[RawError](frankfurter_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_providers(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Provider], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns available exchange rate data providers with their base currency.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.get_providers()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Provider]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.get_providers()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Provider]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](frankfurter_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](frankfurter_api/core/results.py)&#91;list&#91;[Provider](frankfurter_api/models/provider.py)&#93;, [RawError](frankfurter_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Provider](frankfurter_api/models/provider.py)&#93;</code> -- Available providers

**On `Failure`**: `error` is <code>[RawError](frankfurter_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_rate(base: str, quote: str, *, date: Date | None = None, providers: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Rate, GetRateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the blended exchange rate for a single currency pair. Without a date param, returns the latest rate. A same-currency pair returns the identity rate of 1.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.get_rate(base, quote)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Rate
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetRateErrorBody
```

**Async**

```python
result = await async_client.with_raw_response.get_rate(base, quote)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Rate
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetRateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>base</code> | <code>str</code> | Value sent with the request. |
| <code>quote</code> | <code>str</code> | Value sent with the request. |
| <code>date</code> | <code>Date \| None</code> | Specific date (YYYY-MM-DD). Cannot be combined with from/to.<br>**Default**: <code>None</code> |
| <code>providers</code> | <code>str \| None</code> | Comma-separated list of data providers to include<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](frankfurter_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](frankfurter_api/core/results.py)&#91;[Rate](frankfurter_api/models/rate.py), [GetRateErrorBody](frankfurter_api/errors/get_rate_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Rate](frankfurter_api/models/rate.py)</code> -- Exchange rate

**On `Failure`**: `error` is <code>[GetRateErrorBody](frankfurter_api/errors/get_rate_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[NotFound1](frankfurter_api/models/not_found1.py)</code> |
| 422 | <code>[UnprocessableEntity1](frankfurter_api/models/unprocessable_entity1.py)</code> |
| 503 | <code>[ServiceUnavailable1](frankfurter_api/models/service_unavailable1.py)</code> |
| anything unmapped | <code>[RawError](frankfurter_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_rates(*, date: Date | None = None, from_: Date | None = None, to: Date | None = None, base: str | None = "EUR", quotes: str | None = None, providers: str | None = None, group: GroupOrStr | None = None, expand: ExpandOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Rate], GetRatesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns exchange rates blended across providers. Without date params, returns the latest rates. Each record is a single currency pair. The response includes an identity record for the base currency (base equals quote, rate 1), subject to the quotes filter like any other record. Daily date ranges of any length are served, including full history. Limit: requests using `providers` or `expand=providers` recompute the blend per date, so at daily granularity they return 422 for ranges longer than 5 years. With `providers` naming at most 5 providers, a `quotes` list of at most 5 currencies lifts the cap; without `providers`, `expand=providers` ranges compute every currency regardless of `quotes`, so aggregate with `group=week` or `group=month`, add `providers`, or split the range into shorter requests.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.get_rates()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Rate]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetRatesErrorBody
```

**Async**

```python
result = await async_client.with_raw_response.get_rates()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Rate]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetRatesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>date</code> | <code>Date \| None</code> | Specific date (YYYY-MM-DD). Cannot be combined with from/to.<br>**Default**: <code>None</code> |
| <code>from_</code> | <code>Date \| None</code> | Start of date range (YYYY-MM-DD)<br>**Default**: <code>None</code> |
| <code>to</code> | <code>Date \| None</code> | End of date range (YYYY-MM-DD). Defaults to today.<br>**Default**: <code>None</code> |
| <code>base</code> | <code>str \| None</code> | Base currency (default: EUR)<br>**Default**: <code>"EUR"</code> |
| <code>quotes</code> | <code>str \| None</code> | Comma-separated list of quote currencies to include<br>**Default**: <code>None</code> |
| <code>providers</code> | <code>str \| None</code> | Comma-separated list of data providers to include<br>**Default**: <code>None</code> |
| <code>group</code> | <code>[GroupOrStr](frankfurter_api/models/enums/group.py) \| None</code> | Downsample rates by time period. Only applies to date ranges.<br>**Default**: <code>None</code> |
| <code>expand</code> | <code>[ExpandOrStr](frankfurter_api/models/enums/expand.py) \| None</code> | Comma-separated list of optional fields to include per record. Currently supports `providers`, which adds an array of `{ key, date, rate }` objects per record showing each provider's individual observation date and rate. Outliers excluded from the blend (and providers whose rate was overridden by a currency peg) are flagged with `excluded: true`. The field is omitted on synthesized peg rows where no provider published the quote. In CSV output, the `providers` column is encoded as `KEY:RATE` pairs joined by `\|`, with a trailing `*` on excluded entries (e.g. `ECB:0.92\|FED:1.50*`).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](frankfurter_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](frankfurter_api/core/results.py)&#91;list&#91;[Rate](frankfurter_api/models/rate.py)&#93;, [GetRatesErrorBody](frankfurter_api/errors/get_rates_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Rate](frankfurter_api/models/rate.py)&#93;</code> -- Exchange rates

**On `Failure`**: `error` is <code>[GetRatesErrorBody](frankfurter_api/errors/get_rates_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[NotFound1](frankfurter_api/models/not_found1.py)</code> |
| 422 | <code>[UnprocessableEntity1](frankfurter_api/models/unprocessable_entity1.py)</code> |
| 503 | <code>[ServiceUnavailable1](frankfurter_api/models/service_unavailable1.py)</code> |
| anything unmapped | <code>[RawError](frankfurter_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

