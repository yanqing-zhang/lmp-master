'''
@Project ：tortoise-orm-samples 
@File    ：user_controller.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/24 11:25 
'''
from fastapi import FastAPI,APIRouter
from dao.user_dao import UserDao
router = APIRouter()
@router.get("/")
async def get_user_by_login_name():
    login_name = "admin"
    user = await UserDao.get_user_by_login_name(login_name)
    print(f"login_name:{user.login_name},password:{user.login_password}")
    return "success"