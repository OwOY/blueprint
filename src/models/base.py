from datetime import datetime
from sqlalchemy import VARCHAR, ARRAY, INTEGER, BOOLEAN, FLOAT, JSON, TIMESTAMP, func
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


def interger_column(default: int = 0, nullable: bool = True, **kwargs):
    return mapped_column(INTEGER(), default=default, nullable=nullable, **kwargs)

def column_id():
    return mapped_column(primary_key=True, autoincrement=True)

def string_column(
    length: int | None = None, 
    default: str | None = '', 
    nullable: bool = True,
    **kwargs
):
    return mapped_column(
        VARCHAR(length), default=default, nullable=nullable, **kwargs
    )

def reference_uuid_column(comment=''):
    return string_column(length=42, nullable=True, comment=comment)

def float_column(default: float = 0.0, **kwargs):
    return mapped_column(FLOAT(), default=default, **kwargs, nullable=True)

def uuid_column():
    # TODO : 理論上應該是 nullable=False，但考慮到目前資料庫中已有部分資料的 uuid 欄位為 null
    # 因此暫時設為 nullable=True，未來可以逐步清理資料後再改回 nullable=False
    return string_column(length=42, nullable=True, unique=True, comment='uuid')

def json_column(default: dict = None, **kwargs):
    # TODO : 若無必要需求，可以考慮改成 varchar，避免使用 json 型別在不同資料庫的相容性問題
    # 如果可以，nullable=False 會比較好，避免資料不完整的問題
    # 但目前資料庫中已有部分資料的 json 欄位為 null，因此暫時設為 nullable=True
    # 未來可以逐步清理資料後再改回 nullable=False
    default = {} if default is None else default
    return mapped_column(JSON(), default=default, nullable=True, **kwargs)

def list_string_column(
    default: list = None, **kwargs
):
    # TODO : 同上，考慮到目前資料庫中已有部分資料的 list_string 欄位為 null，因此暫時設為 nullable=True
    default = [] if default is None else default
    return mapped_column(ARRAY(VARCHAR()), default=default, **kwargs, nullable=True)

def list_integer_column(
    default: list = None, **kwargs
):
    # TODO : 同上，考慮到目前資料庫中已有部分資料的 list_integer 欄位為 null，因此暫時設為 nullable=True
    default = [] if default is None else default
    return mapped_column(ARRAY(INTEGER()), default=default, **kwargs, nullable=True)

def list_json_column(
    default: list = None, **kwargs
):
    # TODO : 同上，考慮到目前資料庫中已有部分資料的 list_json 欄位為 null，因此暫時設為 nullable=True
    default = [] if default is None else default
    return mapped_column(ARRAY(JSON()), default=default, **kwargs, nullable=True)

def datetime_column(**kwargs):
    return mapped_column(
        TIMESTAMP(timezone=True), 
        server_default=func.now(),
        **kwargs
    )

def bool_column(default: bool = False, **kwargs):
    # TODO : 同上，考慮到目前資料庫中已有部分資料的 bool 欄位為 null，因此暫時設為 nullable=True
    return mapped_column(BOOLEAN(), default=default, nullable=True, **kwargs)

class Base(DeclarativeBase):
    id: Mapped[int] = column_id()
    uuid: Mapped[str] = uuid_column() # 每筆資料都建議有一個 uuid 欄位，方便追蹤與管理
    create_at: Mapped[datetime] = datetime_column(comment="創建時間")
    update_at: Mapped[datetime] = datetime_column(
        onupdate=func.now(), comment="更新時間")
    create_by: Mapped[str] = string_column(
        length=42, default='system', comment="創建人員ID"
    )
    update_by: Mapped[str] = string_column(
        length=42, default='system', comment="更新人員ID"
    )
    is_delete: Mapped[bool] = bool_column(comment="是否刪除")
