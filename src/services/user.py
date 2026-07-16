from repositories.user import UserRepository
from schemas.input.user import CreateUserInput


class SrvUser:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def get_user(self, user_id: str):
        user = await self.repo.get_by_id(user_id)
        return user
    
    async def create_user(
        self, 
        payload: CreateUserInput
    ):
        # 業務邏輯協調
        save_id = await self.repo.create(payload)
        return save_id