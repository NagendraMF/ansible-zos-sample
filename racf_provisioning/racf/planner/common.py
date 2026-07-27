from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Plan:
    operations: list[Any] = field(default_factory=list)
