from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends
from infra.db import get_db_session



SessionDI = Annotated[AsyncSession, Depends(get_db_session)]