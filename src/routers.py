from fastapi import APIRouter, FastAPI, Depends

from apis.user import router as user_router
from cores.security import verify_token


def include_routers(app:FastAPI):
     # 全局依賴驗證 token 的路由器
    token_verify_router = APIRouter(
        dependencies=[Depends(verify_token)]
    )
    app.include_router(user_router)
    # token_verify_router.include_router(system_router)