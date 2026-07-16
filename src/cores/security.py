import jwt
from datetime import datetime, timedelta, timezone
from cores.config import settings
from cores.exception import CryptoException
from utils.time import get_current_time


def encode_jwt(
    payload: dict, 
    secret_key: str = settings.JWT_KEY, 
    expires_seconds: int | None = None
) -> str:
    """
    生成 JWT
    Args:
        payload (dict): 要加密的資料 (業務邏輯應該在外面組裝好)
        secret_key (str): JWT 密鑰
        expires_seconds (int | None): 多少秒後過期，None 表示不設置過期時間
    Returns:
        token (str): 生成的 JWT 字串
    """
    if expires_seconds is not None:
        expire_time = get_current_time() + timedelta(seconds=expires_seconds)
        payload["exp"] = expire_time

    return jwt.encode(payload, key=secret_key, algorithm="HS256")