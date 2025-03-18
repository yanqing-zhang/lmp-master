'''
@Project ：jwt-sample 
@File    ：models.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/15 15:41 
'''
from tortoise import fields, models
from pydantic import BaseModel, ConfigDict

class User(models.Model):
    id = fields.IntField(pk=True, auto_increment=True)
    username = fields.CharField(max_length=20, unique=True)
    hashed_password = fields.CharField(max_length=128)

