# Reference

**Parsed** endpoints return the typed payload and raise `ApiError` on a documented non-2xx. For the raw endpoints, see [Raw API Reference](raw-api-reference.md).

> Source: [FrankfurterClient](frankfurter/client.py)

<details>
<summary><code>def get_currencies(*, scope: ScopeOrStr | None = None, providers: str | None = None, request_options: RequestOptionsOrDict | None = None) -> list[Currency]</code></summary>

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
try:
    response = client.get_currencies()
    # TODO: Handle 'response' of type list[Currency]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.get_currencies()
    # TODO: Handle 'response' of type list[Currency]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>scope</code> | <code>[ScopeOrStr](frankfurter/models/enums/scope.py) \| None</code> | Set to 'all' to include legacy currencies<br>**Default**: <code>None</code> |
| <code>providers</code> | <code>str \| None</code> | Comma-separated list of data providers to include<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](frankfurter/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[Currency](frankfurter/models/currency.py)&#93;</code> -- Available currencies

**OnError**: <code>[ApiError](frankfurter/core/exceptions.py)&#91;[RawError](frankfurter/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_currency(code: str, *, request_options: RequestOptionsOrDict | None = None) -> CurrencyDetail</code></summary>

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
try:
    response = client.get_currency(code)
    # TODO: Handle 'response' of type CurrencyDetail
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCurrencyErrorBody
```

**Async**

```python
try:
    response = await async_client.get_currency(code)
    # TODO: Handle 'response' of type CurrencyDetail
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCurrencyErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>code</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](frankfurter/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CurrencyDetail](frankfurter/models/currency_detail.py)</code> -- Currency details

**OnError**: <code>[ApiError](frankfurter/core/exceptions.py)&#91;[GetCurrencyErrorBody](frankfurter/errors/get_currency_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[NotFound1](frankfurter/models/not_found1.py)</code> |
| anything unmapped | <code>[RawError](frankfurter/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_providers(*, request_options: RequestOptionsOrDict | None = None) -> list[Provider]</code></summary>

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
try:
    response = client.get_providers()
    # TODO: Handle 'response' of type list[Provider]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.get_providers()
    # TODO: Handle 'response' of type list[Provider]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](frankfurter/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[Provider](frankfurter/models/provider.py)&#93;</code> -- Available providers

**OnError**: <code>[ApiError](frankfurter/core/exceptions.py)&#91;[RawError](frankfurter/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_rate(base: str, quote: str, *, date: Date | None = None, providers: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Rate</code></summary>

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
try:
    response = client.get_rate(base, quote)
    # TODO: Handle 'response' of type Rate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetRateErrorBody
```

**Async**

```python
try:
    response = await async_client.get_rate(base, quote)
    # TODO: Handle 'response' of type Rate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetRateErrorBody
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
| <code>request_options</code> | <code>[RequestOptionsOrDict](frankfurter/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Rate](frankfurter/models/rate.py)</code> -- Exchange rate

**OnError**: <code>[ApiError](frankfurter/core/exceptions.py)&#91;[GetRateErrorBody](frankfurter/errors/get_rate_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[NotFound1](frankfurter/models/not_found1.py)</code> |
| 422 | <code>[UnprocessableEntity1](frankfurter/models/unprocessable_entity1.py)</code> |
| 503 | <code>[ServiceUnavailable1](frankfurter/models/service_unavailable1.py)</code> |
| anything unmapped | <code>[RawError](frankfurter/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_rates(*, date: Date | None = None, from_: Date | None = None, to: Date | None = None, base: str | None = "EUR", quotes: str | None = None, providers: str | None = None, group: GroupOrStr | None = None, expand: ExpandOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> list[Rate]</code></summary>

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
try:
    response = client.get_rates()
    # TODO: Handle 'response' of type list[Rate]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetRatesErrorBody
```

**Async**

```python
try:
    response = await async_client.get_rates()
    # TODO: Handle 'response' of type list[Rate]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetRatesErrorBody
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
| <code>group</code> | <code>[GroupOrStr](frankfurter/models/enums/group.py) \| None</code> | Downsample rates by time period. Only applies to date ranges.<br>**Default**: <code>None</code> |
| <code>expand</code> | <code>[ExpandOrStr](frankfurter/models/enums/expand.py) \| None</code> | Comma-separated list of optional fields to include per record. Currently supports `providers`, which adds an array of `{ key, date, rate }` objects per record showing each provider's individual observation date and rate. Outliers excluded from the blend (and providers whose rate was overridden by a currency peg) are flagged with `excluded: true`. The field is omitted on synthesized peg rows where no provider published the quote. In CSV output, the `providers` column is encoded as `KEY:RATE` pairs joined by `\|`, with a trailing `*` on excluded entries (e.g. `ECB:0.92\|FED:1.50*`).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](frankfurter/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[Rate](frankfurter/models/rate.py)&#93;</code> -- Exchange rates

**OnError**: <code>[ApiError](frankfurter/core/exceptions.py)&#91;[GetRatesErrorBody](frankfurter/errors/get_rates_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[NotFound1](frankfurter/models/not_found1.py)</code> |
| 422 | <code>[UnprocessableEntity1](frankfurter/models/unprocessable_entity1.py)</code> |
| 503 | <code>[ServiceUnavailable1](frankfurter/models/service_unavailable1.py)</code> |
| anything unmapped | <code>[RawError](frankfurter/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

