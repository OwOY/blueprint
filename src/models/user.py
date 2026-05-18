from models.base import Base, string_column
from sqlalchemy.orm import Mapped

class ObjUser(Base):
    __tablename__ = 'TBL_USER'
    # 開始定義
    name: Mapped[str] = string_column(length=50, nullable=False)
    email: Mapped[str] = string_column(length=100, nullable=False)
