'''
@Project ：tortoise-orm-samples 
@File    ：user_dao.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/24 11:11 
'''
from typing import Type

from tortoise.contrib.pydantic import PydanticModel
from tortoise.transactions import atomic

from models.permissions import User, UserRoleAssocations


class UserDao:

    # 根据登录名获取用户
    async def get_user_by_login_name(login_name: str) -> User:
        """
        根据登录名获取用户
        :return: 返回查询结果
        """
        user = await User.filter(login_name=login_name).first()
        return user

    @staticmethod
    async def create_user(user: Type[PydanticModel]):
        user_dict = user.model_dump()  # 转为字典
        await User.create(**user_dict)  # 使用 ** 解包字典
        return True

    @atomic()
    async def create_user_role(user: Type[PydanticModel], user_role: Type[PydanticModel]):
        user_dict = user.model_dump()
        user_role_dict = user_role.model_dump()
        await User.create(**user_dict)  # 使用 ** 解包字典
        await UserRoleAssocations.create(**user_role_dict)  # 使用 ** 解包字典
        return True
