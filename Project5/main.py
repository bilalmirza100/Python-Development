from fastapi import FastAPI
from sqlalchemy import text
from app.database import engine
from app.routes import router

app = FastAPI(title="Easy Marketplace API")
app.include_router(router, prefix="/api")

@app.get("/health")
async def health_check():
    """Live health check verifying database connection."""
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        return {"status": "online", "database": "connected"}
    except Exception as e:
        return {"status": "degraded", "database": str(e)}

@app.get("/")
async def root():
    return {"message": "Welcome to the Easy Marketplace API!"}