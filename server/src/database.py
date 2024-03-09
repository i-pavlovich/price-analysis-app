from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from .config import settings


engine = create_async_engine(url=settings.DATABASE_URL, echo=True)
sessionmaker = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with sessionmaker() as session:
        yield session
