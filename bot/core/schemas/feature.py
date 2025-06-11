from pydantic import BaseModel


class FeatureData(BaseModel):
    name: str
    text: str
    triggers: list[str]
    description: str = ""
    error_text: str | None = None
