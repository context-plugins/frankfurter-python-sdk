
# Provider

*This model accepts additional fields of type Any.*

## Structure

`Provider`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Required | Provider identifier |
| `name` | `str` | Required | Full provider name |
| `country_code` | `str` | Optional | ISO 3166-1 alpha-2 country code |
| `rate_type` | `str` | Optional | Official rate type as used by the source |
| `pivot_currency` | `str` | Optional | Base currency for published rates |
| `data_url` | `str` | Optional | Link to the data source |
| `terms_url` | `str` | Optional | Link to terms of use |
| `start_date` | `date` | Optional | Earliest available date |
| `end_date` | `date` | Optional | Latest available date |
| `publish_cadence` | [`PublishCadence`](../../doc/models/publish-cadence.md) | Optional | How often the provider publishes rates. Determines the unit of publishes_missed: a count of days, ISO weeks, or calendar months. Null for historical-only providers with no scheduled cadence. |
| `publishes_missed` | `int` | Optional | Number of expected publishes missed since end_date, in units of publish_cadence. For daily providers, counts scheduled publish days strictly between end_date and today. For weekly and monthly providers, counts ISO weeks or calendar months between the latest imported bucket and the bucket whose publish window has already started. Null when the provider has no scheduled cadence or no imported data.<br><br>**Constraints**: `>= 0` |
| `currencies` | `List[str]` | Required | Currency codes covered by this provider |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from frankfurterapi.models.provider import Provider

provider = Provider(
    key='key8',
    name='name8',
    currencies=[
        'currencies7'
    ],
    country_code='country_code8',
    rate_type='rate_type4',
    pivot_currency='pivot_currency0',
    data_url='data_url4',
    terms_url='terms_url6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

