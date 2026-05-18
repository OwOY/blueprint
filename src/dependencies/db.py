from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from cores.config import Settings


settings = Settings()
uri = settings.database_url
engine = create_async_engine(uri, echo=True)

session_local = async_sessionmaker(engine, expire_on_commit=False)

async def get_db_session():
    """Dependency function to get a database session."""
    async with session_local() as session:
        try:
            yield session
        except:
            await session.rollback()
            raise
        finally:
            await session.close()
    

DBSession = Annotated[AsyncSession, Depends(get_db_session)]