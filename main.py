from fastapi import FastAPI

from routes import calculator, health,history

from database import engine, Base
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Calculator API",
    version="1.0.0"
)

app.include_router(health.router)
app.include_router(calculator.router)
app.include_router(history.router)