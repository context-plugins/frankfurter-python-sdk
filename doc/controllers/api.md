# API

```python
client_api = client.client
```

## Class Name

`Api`

## Methods

* [Get Rates](../../doc/controllers/api.md#get-rates)
* [Get Rate](../../doc/controllers/api.md#get-rate)
* [Get Currency](../../doc/controllers/api.md#get-currency)
* [Get Currencies](../../doc/controllers/api.md#get-currencies)
* [Get Providers](../../doc/controllers/api.md#get-providers)


# Get Rates

Returns exchange rates blended across providers. Without date params, returns the latest rates. Each record is a single currency pair. The response includes an identity record for the base currency (base equals quote, rate 1), subject to the quotes filter like any other record. Daily date ranges of any length are served, including full history. Limit: requests using `providers` or `expand=providers` recompute the blend per date, so at daily granularity they return 422 for ranges longer than 5 years. With `providers` naming at most 5 providers, a `quotes` list of at most 5 currencies lifts the cap; without `providers`, `expand=providers` ranges compute every currency regardless of `quotes`, so aggregate with `group=week` or `group=month`, add `providers`, or split the range into shorter requests.

```python
def get_rates(self,
             date=None,
             mfrom=None,
             to=None,
             base="EUR",
             quotes=None,
             providers=None,
             group=None,
             expand=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date` | `date` | Query, Optional | Specific date (YYYY-MM-DD). Cannot be combined with from/to. |
| `mfrom` | `date` | Query, Optional | Start of date range (YYYY-MM-DD) |
| `to` | `date` | Query, Optional | End of date range (YYYY-MM-DD). Defaults to today. |
| `base` | `str` | Query, Optional | Base currency (default: EUR)<br><br>**Default**: `"EUR"` |
| `quotes` | `str` | Query, Optional | Comma-separated list of quote currencies to include |
| `providers` | `str` | Query, Optional | Comma-separated list of data providers to include |
| `group` | [`Group`](../../doc/models/group.md) | Query, Optional | Downsample rates by time period. Only applies to date ranges. |
| `expand` | [`Expand`](../../doc/models/expand.md) | Query, Optional | Comma-separated list of optional fields to include per record. Currently supports `providers`, which adds an array of `{ key, date, rate }` objects per record showing each provider's individual observation date and rate. Outliers excluded from the blend (and providers whose rate was overridden by a currency peg) are flagged with `excluded: true`. The field is omitted on synthesized peg rows where no provider published the quote. In CSV output, the `providers` column is encoded as `KEY:RATE` pairs joined by `\|`, with a trailing `*` on excluded entries (e.g. `ECB:0.92\|FED:1.50*`). |

## Response Type

**200**: Exchange rates

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[Rate]`](../../doc/models/rate.md).

## Example Usage

```python
date = dateutil.parser.parse('2024-01-15').date()

mfrom = dateutil.parser.parse('2024-01-01').date()

to = dateutil.parser.parse('2024-01-31').date()

base = 'USD'

quotes = 'USD,GBP,JPY'

providers = 'ECB,TCMB'

group = Group.MONTH

expand = Expand.PROVIDERS

result = client_api.get_rates(
    date=date,
    mfrom=mfrom,
    to=to,
    base=base,
    quotes=quotes,
    providers=providers,
    group=group,
    expand=expand
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
[
  {
    "date": "2024-01-15",
    "base": "EUR",
    "quote": "EUR",
    "rate": 1.0
  },
  {
    "date": "2024-01-15",
    "base": "EUR",
    "quote": "GBP",
    "rate": 0.8623
  },
  {
    "date": "2024-01-15",
    "base": "EUR",
    "quote": "USD",
    "rate": 1.089
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | No data found | [`NotFoundException`](../../doc/models/not-found-exception.md) |
| 422 | Invalid request | [`UnprocessableEntityException`](../../doc/models/unprocessable-entity-exception.md) |
| 503 | The request deadline expired before the response could be computed. Retry with a narrower request: filter with quotes, aggregate with group, or split the range into shorter requests. | [`ServiceUnavailableException`](../../doc/models/service-unavailable-exception.md) |


# Get Rate

Returns the blended exchange rate for a single currency pair. Without a date param, returns the latest rate. A same-currency pair returns the identity rate of 1.

```python
def get_rate(self,
            base,
            quote,
            date=None,
            providers=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `base` | `str` | Template, Required | - |
| `quote` | `str` | Template, Required | - |
| `date` | `date` | Query, Optional | Specific date (YYYY-MM-DD). Cannot be combined with from/to. |
| `providers` | `str` | Query, Optional | Comma-separated list of data providers to include |

## Response Type

**200**: Exchange rate

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Rate`](../../doc/models/rate.md).

## Example Usage

```python
base = 'EUR'

quote = 'USD'

date = dateutil.parser.parse('2024-01-15').date()

providers = 'ECB,TCMB'

result = client_api.get_rate(
    base,
    quote,
    date=date,
    providers=providers
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "date": "2026-03-25",
  "base": "EUR",
  "quote": "USD",
  "rate": 1.1568
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | No data found | [`NotFoundException`](../../doc/models/not-found-exception.md) |
| 422 | Invalid request | [`UnprocessableEntityException`](../../doc/models/unprocessable-entity-exception.md) |
| 503 | The request deadline expired before the response could be computed. Retry with a narrower request: filter with quotes, aggregate with group, or split the range into shorter requests. | [`ServiceUnavailableException`](../../doc/models/service-unavailable-exception.md) |


# Get Currency

Returns details for a single currency, including provider information or peg metadata.

```python
def get_currency(self,
                code)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Template, Required | - |

## Response Type

**200**: Currency details

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CurrencyDetail`](../../doc/models/currency-detail.md).

## Example Usage

```python
code = 'USD'

result = client_api.get_currency(code)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "iso_code": "USD",
  "iso_numeric": "840",
  "name": "United States Dollar",
  "symbol": "$",
  "providers": [
    "ECB",
    "BOC",
    "FED"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | No data found | [`NotFoundException`](../../doc/models/not-found-exception.md) |


# Get Currencies

Returns available currencies with their names and date ranges. By default, only active currencies are included.

```python
def get_currencies(self,
                  scope=None,
                  providers=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `scope` | [`Scope`](../../doc/models/scope.md) | Query, Optional | Set to 'all' to include legacy currencies |
| `providers` | `str` | Query, Optional | Comma-separated list of data providers to include |

## Response Type

**200**: Available currencies

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[Currency]`](../../doc/models/currency.md).

## Example Usage

```python
providers = 'ECB,TCMB'

result = client_api.get_currencies(
    providers=providers
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
[
  {
    "iso_code": "EUR",
    "iso_numeric": "978",
    "name": "Euro",
    "symbol": "€",
    "start_date": "1999-01-04",
    "end_date": "2026-03-17"
  },
  {
    "iso_code": "USD",
    "iso_numeric": "840",
    "name": "United States Dollar",
    "symbol": "$",
    "start_date": "1999-01-04",
    "end_date": "2026-03-17"
  }
]
```


# Get Providers

Returns available exchange rate data providers with their base currency.

```python
def get_providers(self)
```

## Response Type

**200**: Available providers

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[Provider]`](../../doc/models/provider.md).

## Example Usage

```python
result = client_api.get_providers()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
[
  {
    "key": "ECB",
    "name": "European Central Bank",
    "country_code": "EU",
    "rate_type": "reference",
    "pivot_currency": "EUR",
    "data_url": "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html",
    "terms_url": "https://www.ecb.europa.eu/services/using-our-site/disclaimer/html/index.en.html",
    "start_date": "1999-01-04",
    "end_date": "2026-03-17",
    "currencies": [
      "USD",
      "GBP"
    ]
  }
]
```

