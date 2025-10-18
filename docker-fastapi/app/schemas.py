from pydantic import BaseModel, Field
from typing import List

class PredictRequest(BaseModel):
    x: List[float] = Field(..., description="Input values")

class PredictResponse(BaseModel):
    input: List[float]
    output: List[float]
