from sqlalchemy.ext.asyncio import AsyncSession

from models.user import ObjUser
from repositories.base import BaseRespository


class UserRepository(BaseRespository[ObjUser]):
    def __init__(self, session: AsyncSession):
        super().__init__(model=ObjUser, session=session)
