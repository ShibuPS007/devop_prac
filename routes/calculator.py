from fastapi import APIRouter

from schemas.calculation_request import CalculationRequest
from schemas.calculation_response import CalculationResponse
from services.calculator_services import perform_calculation
from services.history_services import add_calculation
from datetime import datetime

router = APIRouter()


@router.post("/calculate", response_model=CalculationResponse)
def calculate(request: CalculationRequest):

    result = perform_calculation(
        request.a,
        request.b,
        request.operation
    )

    calculation = {
        "a": request.a,
        "b": request.b,
        "operation": request.operation,
        "result": result,
        "created_at":datetime.now()
    }

    saved_calculation = add_calculation(calculation)

    return saved_calculation