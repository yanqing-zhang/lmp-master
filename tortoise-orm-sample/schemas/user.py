'''
@Project ：tortoise-orm-samples 
@File    ：user.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/24 17:11 
'''
from tortoise.contrib.pydantic import pydantic_model_creator
from models.permissions import User

User_Pydantic = pydantic_model_creator(User, name="User", exclude_readonly=True)