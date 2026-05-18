from schemas.base import Base


class GetUserInput(Base):
    user_id: str
class CreateUserInput(Base):
    name: str
    email: str
    password: str