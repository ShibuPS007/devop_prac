from pydantic import BaseModel
from enum import Enum


class Operation(str, Enum):
    add = "add"
    subtract = "subtract"
    multiply = "multiply"
    divide = "divide"
    power = "power"
    modulus = "modulus"


class CalculationRequest(BaseModel):
    a: float
    b: float
    operation: Operation