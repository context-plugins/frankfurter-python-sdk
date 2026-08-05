
# Provider 2

*This model accepts additional fields of type Any.*

## Structure

`Provider2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Required | Provider key |
| `date` | `date` | Required | Provider observation date used for this entry |
| `rate` | `float` | Required | Provider's rate, rebased to the row's base<br><br>**Constraints**: `> 0` |
| `excluded` | `bool` | Optional | Present and true when this entry did not contribute to the blended rate |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from frankfurterapi.models.provider_2 import Provider2

provider_2 = Provider2(
    key='key8',
    date=dateutil.parser.parse('2016-03-13').date(),
    rate=134.12,
    excluded=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

