from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.api.auth import router as auth_router
from app.api.sweets import router as sweets_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(auth_router)

app.include_router(sweets_router)