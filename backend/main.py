
import os

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text

DATABASE_URL = os.getenv("DATABASE_URL")

# Use psycopg2 driver for PostgreSQL
if DATABASE_URL and DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgresql://",
        "postgresql+psycopg2://",
        1
    )

engine = (
    create_engine(DATABASE_URL, pool_pre_ping=True)
    if DATABASE_URL
    else None
)

app = FastAPI(title="InterviewIQ API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/health/db")
def health_db():
    if engine is None:
        raise HTTPException(
            status_code=503,
            detail="Database not configured"
        )

    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))

        return {"database": "ok"}

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Database unavailable"
        )
