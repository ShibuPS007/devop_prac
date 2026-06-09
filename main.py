from fastapi import FastAPI

app = FastAPI(title="VMSS Demo API")

@app.get("/")
def home():
    return {
        "message": "Hello from FastAPI running through Azure DevOps VMSS agents!"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }