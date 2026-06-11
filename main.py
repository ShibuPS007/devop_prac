from fastapi import FastAPI

app = FastAPI(title="Math API")

# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Math API running successfully!"
    }


# Health check
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/add")
def add(a: int, b: int):
    return {
        "operation": "addition",
        "result": a + b
    }


@app.get("/subtract")
def subtract(a: int, b: int):
    return {
        "operation": "subtraction",
        "result": a - b
    }


@app.get("/divide")
def divide(a: int, b: int):

    if b == 0:
        return {
            "error": "Division by zero not allowed"
        }

    return {
        "operation": "division",
        "result": a / b
    }
