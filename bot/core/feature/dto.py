from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class FeatureData:
    name: str
    text: str
    triggers: list[str]
    description: str = ""
    error_text: Optional[str] = None
