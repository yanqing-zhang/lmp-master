'''
@Project ：tortoise-orm-samples 
@File    ：user_role.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/24 17:14 
'''
from tortoise.contrib.pydantic import pydantic_model_creator
from models.permissions import UserRoleAssocations

UserRoleAssocations_Pydantic = pydantic_model_creator(UserRoleAssocations, name="UserRoleAssocations", exclude_readonly=True)