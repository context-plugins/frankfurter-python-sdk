
# Currency

*This model accepts additional fields of type Any.*

## Structure

`Currency`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `iso_code` | `str` | Required | ISO 4217 currency code |
| `iso_numeric` | `str` | Optional | ISO 4217 numeric code |
| `name` | `str` | Required | Full currency name |
| `symbol` | `str` | Optional | Currency symbol |
| `start_date` | `date` | Optional | Earliest available date |
| `end_date` | `date` | Optional | Latest available date |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from frankfurterapi.models.currency import Currency

currency = Currency(
    iso_code='iso_code0',
    name='name0',
    iso_numeric='iso_numeric8',
    symbol='symbol8',
    start_date=dateutil.parser.parse('2016-03-13').date(),
    end_date=dateutil.parser.parse('2016-03-13').date(),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

