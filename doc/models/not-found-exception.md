
# Not Found Exception

*This model accepts additional fields of type Any.*

## Structure

`NotFoundException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
try:
    # make the API call
except NotFoundException as e:
    print(e)
except ApiException as e:
    print(e)
```

