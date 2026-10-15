import os
from fastapi import FastAPI
from sqlalchemy import create_engine, text

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, pool_pre_ping=True) if DATABASE_URL else None

app = FastAPI(title="InterviewIQ API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/health/db")
def health_db():
    if engine is None:
        return {"database": "not configured"}
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"database": "ok"}
