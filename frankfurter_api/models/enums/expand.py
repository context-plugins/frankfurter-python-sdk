from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Expand(str, Enum):
    PROVIDERS = "providers"

    __str__ = str.__str__


ExpandOrStr: TypeAlias = Annotated[Expand | str, open_enum_validator(Expand)]
