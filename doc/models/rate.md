
# Rate

*This model accepts additional fields of type Any.*

## Structure

`Rate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date` | `date` | Required | The date of the rate |
| `base` | `str` | Required | Base currency code |
| `quote` | `str` | Required | Quote currency code |
| `rate` | `float` | Required | Exchange rate value<br><br>**Constraints**: `> 0` |
| `providers` | [`List[Provider2]`](../../doc/models/provider-2.md) | Optional | Per-provider rates for this pair. Present only when `expand=providers` is set. Each entry has the provider's observation date and published rate (rebased to the row's base). Entries with `excluded: true` did not contribute to the blended `rate` — either flagged as outliers by the consensus filter, or overridden by a currency peg. Omitted on synthesized peg rows where no provider published the quote. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from frankfurterapi.models.provider_2 import Provider2
from frankfurterapi.models.rate import Rate

rate = Rate(
    date=dateutil.parser.parse('2016-03-13').date(),
    base='base6',
    quote='quote0',
    rate=0.01,
    providers=[
        Provider2(
            key='key0',
            date=dateutil.parser.parse('2016-03-13').date(),
            rate=60.2,
            excluded=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

