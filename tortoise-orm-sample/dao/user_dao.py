'''
@Project ：tortoise-orm-samples 
@File    ：user_dao.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/24 11:11 
'''
from models.permissions import User,UserRoleAssocations
from schemas.user import User_Pydantic
from schemas.user_role import UserRoleAssocations_Pydantic
from utils.utils import model_to_dict
class UserDao:

    # 根据登录名获取用户
    async def get_user_by_login_name(login_name: str) -> User:
        """
        根据登录名获取用户
        :return: 返回查询结果
        """
        user = await User.filter(login_name=login_name).first()
        return user

    async def create_user(user_dict: dict, user_role_dict: dict):

        await User.create(user_dict)
        await UserRoleAssocations.create(user_role_dict)
        return True
