from schemas.base import Base


class GetUserOutput(Base):
    id: int
    name: str
    email: str
