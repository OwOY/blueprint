from typing import Annotated

from fastapi import Depends

from repositories.user import UserRepository
from dependencies.db import SessionDI

async def get_user_repository(
    session: SessionDI
) -> UserRepository:
    return UserRepository(session)

UserRepositoryDI = Annotated[UserRepository, Depends(get_user_repository)]