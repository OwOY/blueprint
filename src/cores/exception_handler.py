from fastapi import status
from fastapi import Request
from fastapi.responses import JSONResponse
from cores.response import ApiResponse


class AppException(Exception):
    def __init__(
        self,
        message: str,
        status_code: int = 400,
    ):
        self.message = message
        self.status_code = status_code


async def app_exception_handler(
    request: Request, 
    exc: AppException
):
    return JSONResponse(
        status_code=exc.status_code,
        content=ApiResponse(
            success=False,
            message=exc.message,
            data={},
            code=exc.status_code
        ).model_dump()
    )