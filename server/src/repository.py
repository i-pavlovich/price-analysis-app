import abc

from sqlalchemy import insert, select

from .database import sessionmaker


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    async def add():
        raise NotImplementedError

    @abc.abstractmethod
    async def get():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add(self, data: dict) -> int:
        async with sessionmaker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar_one()

    async def get(self, id: int):
        async with sessionmaker() as session:
            stmt = select(self.model).where(self.model.id == id)
            result = await session.execute(stmt)
            return result.scalar_one()
