
# Currency Detail

*This model accepts additional fields of type Any.*

## Structure

`CurrencyDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `iso_code` | `str` | Required | ISO 4217 currency code |
| `iso_numeric` | `str` | Optional | ISO 4217 numeric code |
| `name` | `str` | Required | Full currency name |
| `symbol` | `str` | Optional | Currency symbol |
| `providers` | `List[str]` | Optional | Provider keys that publish this currency |
| `peg` | [`Peg`](../../doc/models/peg.md) | Optional | Peg metadata, present only for pegged currencies |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from frankfurterapi.models.currency_detail import CurrencyDetail
from frankfurterapi.models.peg import Peg

currency_detail = CurrencyDetail(
    iso_code='iso_code2',
    name='name2',
    iso_numeric='iso_numeric0',
    symbol='symbol4',
    providers=[
        'providers7'
    ],
    peg=Peg(
        base='base8',
        rate=219.78,
        authority='authority6',
        source='source8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

