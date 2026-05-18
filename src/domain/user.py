from typing import Optional
from datetime import datetime
from models.user import ObjUser


class UserDomain:
    def create(self, user_data):
        # 業務規則驗證
        if not self._is_valid_email(user_data.email):
            raise ValueError("Invalid email format")
        # 其他業務邏輯，例如密碼加密、默認值設置等
        
    def _is_valid_password(self, password):
        if '*' in password:
            raise