'''
@Project ：lmp-server-master 
@File    ：dependence.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/12 11:46 
'''
from typing import Optional

import jwt
from fastapi import Depends, Header, HTTPException, Request

from core.ctx import CTX_USER_ID
from models.permission import Role, LoginUser, User
from settings.config import settings
from mock.mock_login_json import create_user

class AuthControl:
    @classmethod
    async def is_authed(cls, token: str = Header(..., description="token验证")) -> Optional["User"]:
        print("================is_authed=====================")
        print(f"token:{token}")
        try:
            if token == "dev":
                user = await create_user()
                user_id = user.user_id
            else:
                decode_data = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.JWT_ALGORITHM)
                user_id = decode_data.get("user_id")
                print(f"#############user_id of decode_data:{user_id}")
            user = await create_user()
            if not user:
                raise HTTPException(status_code=401, detail="Authentication failed")
            CTX_USER_ID.set(int(user_id))
            return user
        except jwt.DecodeError:
            raise HTTPException(status_code=401, detail="无效的Token")
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="登录已过期")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"{repr(e)}")

    async def get_token(self, login_user: LoginUser) -> str:
        data = {"user_id": login_user.user_id, "login_name": login_user.login_name}
        token = jwt.encode(data, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
        return token
class PermissionControl:
    @classmethod
    async def has_permission(cls, request: Request, current_user: User = Depends(AuthControl.is_authed)) -> None:
        print("================has_permission=====================")
        pass
        # if current_user.is_superuser:
        #     return
        # method = request.method
        # path = request.url.path
        # roles: list[Role] = await current_user.roles
        # if not roles:
        #     raise HTTPException(status_code=403, detail="The user is not bound to a role")
        # apis = [await role.apis for role in roles]
        # permission_apis = list(set((api.method, api.path) for api in sum(apis, [])))
        # # path = "/api/v1/auth/userinfo"
        # # method = "GET"
        # if (method, path) not in permission_apis:
        #     raise HTTPException(status_code=403, detail=f"Permission denied method:{method} path:{path}")


DependAuth = Depends(AuthControl.is_authed)
DependPermisson = Depends(PermissionControl.has_permission)
