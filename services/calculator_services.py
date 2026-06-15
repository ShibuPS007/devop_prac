from fastapi import HTTPException


def perform_calculation(a: float, b: float, operation: str):

    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":

        if b == 0:
            raise HTTPException(
                status_code=400,
                detail="Division by zero not allowed"
            )

        return a / b

    elif operation == "power":
        return a ** b

    elif operation == "modulus":

        if b == 0:
            raise HTTPException(
                status_code=400,
                detail="Modulus by zero not allowed"
            )

        return a % b

    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid operation"
        )