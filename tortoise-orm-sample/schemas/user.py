'''
@Project ：tortoise-orm-samples 
@File    ：user.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/24 17:11 
'''
from tortoise.contrib.pydantic import pydantic_model_creator
from models.permissions import User
from datetime import datetime
from dao.user_dao import UserDao
from tortoise import Tortoise
import asyncio
# "latest_login_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
async def insert_user():
    UserDto = pydantic_model_creator(User, name="UserDto", exclude_readonly=True)
    # 直接传入字典初始化 UserDto
    user_data = {
        "login_name": "admin",
        "user_id": "10086",
        "login_password": "xfafdasfw",
        "user_name": "san.li",
        "avatar_url": "/a.jpg",
        "gender": 1,
        "phone_no": "13410102020",
        "email": "san.li@llm.com",
        "wechat_id": "13410102020",
        "create_user": "U10001",
        "update_user": "U10001",
        "yn": 1,
    }
    userDto = UserDto(**user_data)
    print(userDto.model_dump())
    ret = await UserDao.create_user(userDto)
    print(f"ret:{ret}")

async def main():
    await insert_user()
    await Tortoise.close_connections()
if __name__ == '__main__':
    asyncio.run(main())