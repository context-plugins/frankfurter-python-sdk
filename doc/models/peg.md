
# Peg

Peg metadata, present only for pegged currencies

*This model accepts additional fields of type Any.*

## Structure

`Peg`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `base` | `str` | Optional | - |
| `rate` | `float` | Optional | - |
| `authority` | `str` | Optional | - |
| `source` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from frankfurterapi.models.peg import Peg

peg = Peg(
    base='base8',
    rate=219.78,
    authority='authority6',
    source='source8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

