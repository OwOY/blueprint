from fastapi import APIRouter, Depends
from schemas.input.user import CreateUserInput, GetUserInput
from schemas.output.user import GetUserOutput
from cores.repository import UserDep

router = APIRouter(
    prefix="/user",
    tags=["人員相關"],
    # dependencies=[Depends(...)], # 主要放置需要全局依賴的項目，如認證、權限等
    # route_class=... # 可以自定義路由類別，例如添加日誌、錯誤處理等
)

@router.get('/{user_id}', response_model=GetUserOutput)
async def get_user(
    user_service: UserDep,
    params: GetUserInput = Depends(),
):
    return await user_service.get_user(params)
    
@router.post('')
async def create_user(
    params: CreateUserInput,
    user_service: UserDep
):
    return await user_service.create_user(params)