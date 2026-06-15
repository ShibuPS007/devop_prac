from fastapi import APIRouter, HTTPException

from services.history_services import (
    get_all_calculations,
    get_calculation_by_id,
    delete_calculation,
    clear_history
)

router = APIRouter()


@router.get("/history")
def get_history():
    return get_all_calculations()


@router.get("/history/{calc_id}")
def get_calculation(calc_id: int):

    calculation = get_calculation_by_id(calc_id)

    if calculation is None:
        raise HTTPException(
            status_code=404,
            detail="Calculation not found"
        )

    return calculation


@router.delete("/history")
def remove_all():

    clear_history()

    return {
        "message": "History cleared successfully"
    }


@router.delete("/history/{calc_id}")
def remove_calculation(calc_id: int):

    success = delete_calculation(calc_id)

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Calculation not found"
        )

    return {
        "message": "Calculation deleted successfully"
    }