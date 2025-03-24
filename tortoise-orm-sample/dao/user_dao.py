'''
@Project ：tortoise-orm-samples 
@File    ：user_dao.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/24 11:11 
'''
from models.permissions import User
class UserDao:

    # 根据登录名获取用户
    async def get_user_by_login_name(login_name: str) -> User:
        """
        根据登录名获取用户
        :return: 返回查询结果
        """
        user = await User.filter(login_name=login_name).first()

        return user
