
# Service Unavailable Exception

*This model accepts additional fields of type Any.*

## Structure

`ServiceUnavailableException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
try:
    # make the API call
except ServiceUnavailableException as e:
    print(e)
except ApiException as e:
    print(e)
```

