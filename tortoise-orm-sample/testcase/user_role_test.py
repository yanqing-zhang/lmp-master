'''
@Project ：tortoise-orm-sample 
@File    ：user_role_test.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/25 13:27 
'''
from datetime import datetime
from pydantic import BaseModel
from models.permissions import User, UserRoleAssocations
from typing import Any, Dict, Generic, List, NewType, Tuple, Type, TypeVar, Union

def exchange():
    user = User()
    user_type = TypeVar(user,BaseModel)
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

