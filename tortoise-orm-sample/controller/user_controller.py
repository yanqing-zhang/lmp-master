'''
@Project ：tortoise-orm-samples 
@File    ：user_controller.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/24 11:25 
'''
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from fastapi import FastAPI,APIRouter

from utils.utils import model_to_dict,model_to_dict_with_exclude
from dao.user_dao import UserDao
from models.permissions import User, UserRoleAssocations

router = APIRouter()
@router.get("/")
async def get_user_by_login_name():
    login_name = "admin"
    user = await UserDao.get_user_by_login_name(login_name)
    print(f"login_name:{user.login_name},password:{user.login_password}")
    return "success"

@router.post("/create")
async def create_user_with_roles():
    user = User()
    user.login_name = "admin"
    user.user_id = "10086"
    user.login_password = "xfafdasfw"
    user.user_name = "san.li"
    user.avatar_url = "/a.jpg"
    user.latest_login_at = datetime.now()
    user.gender = 1
    user.phone_no = "13410102020"
    user.email = "san.li@llm.com"
    user.wechat_id = "13410102020"
    user.create_user_id = "U10001"
    user.update_user_id = "U10001"
    user.create_at = datetime.now()
    user.update_at = datetime.now()
    user.yn = 1
    user_role = UserRoleAssocations()
    user_role.user_id = "10086"
    user_role.role_id = "R1002"
    user_dict = model_to_dict_with_exclude(user,exclude=["id"])
    user_role_dict = model_to_dict_with_exclude(user_role,exclude=["id"])
    print(f"user_dict:{user_dict}")
    ret = await UserDao.create_user(user_dict,user_role_dict)
    return "success"
