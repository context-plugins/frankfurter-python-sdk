
# Unprocessable Entity Exception

*This model accepts additional fields of type Any.*

## Structure

`UnprocessableEntityException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
try:
    # make the API call
except UnprocessableEntityException as e:
    print(e)
except ApiException as e:
    print(e)
```

