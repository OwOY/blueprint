from typing import Annotated

from fastapi import Depends
from services.user import SrvUser
from dependencies.repository import UserRepositoryDI


async def get_user_service(
    repo: UserRepositoryDI
) -> SrvUser:
    return SrvUser(repo)


UserServiceDI = Annotated[SrvUser, Depends(get_user_service)]