from typing import List

from pydantic import BaseModel


class ResultSchema(BaseModel):
    photo_id: int
    model_type: str
    result: List[dict]
