from typing import Annotated
from fastapi import Depends

from dependencies.db import DBSession
from services.user import SrvUser


async def get_user_repository(session: DBSession) -> SrvUser:
    return SrvUser(session)

UserDep = Annotated[SrvUser, Depends(get_user_repository)]
