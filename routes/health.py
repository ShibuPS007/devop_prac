from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Calculator API running successfully"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }