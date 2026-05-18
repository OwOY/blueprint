from uuid import uuid4
from typing import Type, TypeVar, Generic

from sqlalchemy import select, update
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession

from utils import timenow

T = TypeVar('T', bound=DeclarativeBase)

class BaseRespository(Generic[T]):
    def __init__(self, model: Type[T], session: AsyncSession):
        self.model = model
        self.session = session
    
    def make_fts(self, **kwargs):
        """建立篩選列表
        Args:
            **kwargs: 欄位名稱和對應的值，格式為 field=value
        Returns:
            fts: 組合後的全文檢索字串
        """
        filters = [
            getattr(self.model, field) == value
            for field, value in kwargs.items()
        ]
        return filters
    
    async def get(self, **kwargs) -> T | None:
        """取得單筆資料，支援條件篩選
        Args:
            **kwargs: 篩選條件，格式為 field=value
        Returns:
            obj: 符合條件的資料，若無則回傳 None
        """
        filters = self.make_fts(**kwargs)
        stmt = select(self.model).where(*filters)
        result = await self.session.execute(stmt)
        return result.scalars().first()
    
    async def get_list(
        self, order_by: list | None = None, **kwargs
    ) -> list[T]:
        """取得多筆資料，支援條件篩選和排序
        Args:
            order_by: 排序條件，格式為 list[Model.field.asc() | Model.field.desc()]
            **kwargs: 篩選條件，格式為 field=value
        Returns:
            objs: 符合條件的資料列表
        """
        filters = self.make_fts(**kwargs)
        stmt = select(self.model).where(*filters)
        if order_by:
            stmt = stmt.order_by(order_by)
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    async def get_by_id(self, uuid) -> T | None:
        """Get a record by its ID."""
        result = await self.get(uuid=uuid)
        return result
    
    async def create(self, data: dict, user: str = 'system') -> str:
        """Create a new record in the database."""
        obj_id = str(uuid4())
        data['uuid'] = obj_id
        data['create_at'] = timenow()
        data['create_by'] = user
        data['update_at'] = timenow()
        data['update_by'] = user
        
        obj = self.model(**data)
        self.session.add(obj)
        await self.session.flush()
        return obj_id
    
    async def update(self, uuid, data: dict, user: str = 'system') -> None:
        data['update_at'] = timenow()
        data['update_by'] = user
        stmt = update(self.model)\
            .where(self.model.uuid == uuid)\
            .values(**data)
        await self.session.execute(stmt)
    
    async def delete(self, uuid, user: str = 'system') -> None:
        await self.update(uuid, {'is_delete': True}, user=user)
    
    async def delete_by_id(self, uuid, user: str = 'system') -> None:
        """Delete a record by its ID."""
        await self.delete(uuid=uuid, user=user)