import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .database import get_session

app = FastAPI()


@app.get("/")
def health_check() -> dict[str, str]:
    return {"HealthCheck": "OK"}


@app.get("/test-db")
def test_database(session: AsyncSession = Depends(get_session)) -> dict[str, str]:
    return {"DatabaseStatus": "OK"}


if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True)
