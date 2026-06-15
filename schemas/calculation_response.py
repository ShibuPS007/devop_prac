from pydantic import BaseModel
from datetime import datetime

class CalculationResponse(BaseModel):
    id: int
    a: float
    b: float
    operation: str
    result: float
    created_at: datetime