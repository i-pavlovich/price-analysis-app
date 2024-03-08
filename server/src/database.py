from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from .config import settings


_engine = create_async_engine(url=settings.DATABASE_URL, echo=True)
_sessionmaker = async_sessionmaker(bind=_engine, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with _sessionmaker() as session:
        yield session
