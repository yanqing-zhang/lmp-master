'''
@Project ：tortoise-orm-samples 
@File    ：user_controller.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/24 11:25 
'''
from datetime import datetime
from fastapi import FastAPI,APIRouter

from dao.user_dao import UserDao
from models.permissions import User, UserRoleAssocations
from tortoise.contrib.pydantic import pydantic_model_creator
router = APIRouter()
@router.get("/")
async def get_user_by_login_name():
    login_name = "admin"
    user = await UserDao.get_user_by_login_name(login_name)
    print(f"login_name:{user.login_name},password:{user.login_password}")
    return "success"

@router.post("/create")
async def create_user_with_roles():
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
    # print(userDto.model_dump())
    UserRoleAssocationsDto = pydantic_model_creator(UserRoleAssocations, name="UserRoleAssocationsDto", exclude_readonly=True)
    # 直接传入字典初始化 UserRoleAssocationsDto
    user_role_data = {
        "user_id": user_data.get("user_id"),
        "role_id": "R1002",
        "create_user": "U10001",
        "update_user": "U10001",
        "yn": 1,
    }
    userRoleAssocationsDto = UserRoleAssocationsDto(**user_role_data)
    ret = await UserDao.create_user_role(userDto, userRoleAssocationsDto)
    return "success"
