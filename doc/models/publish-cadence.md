
# Publish Cadence

How often the provider publishes rates. Determines the unit of publishes_missed: a count of days, ISO weeks, or calendar months. Null for historical-only providers with no scheduled cadence.

## Enumeration

`PublishCadence`

## Fields

| Name |
|  --- |
| `DAILY` |
| `WEEKLY` |
| `MONTHLY` |

## Example

```python
from frankfurterapi.models.publish_cadence import PublishCadence

publish_cadence = PublishCadence.DAILY
```

