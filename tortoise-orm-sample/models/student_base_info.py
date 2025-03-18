'''
@Project ：tortoise-orm-sample 
@File    ：student_base_info.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/17 11:22 
'''
from tortoise import fields
from tortoise.models import Model

class Student(Model):
    id = fields.IntField(pk=True, autoincrement=True)
    stu_name = fields.CharField(max_length=20, description="学生姓名")
    stu_gender = fields.IntField(description="学生性别")
    stu_birthday = fields.DatetimeField(description="学生生日")
    stu_no = fields.CharField(max_length=20, description="学号")
    yn = fields.IntField(description="数据是否有效")

    class Meta:
        table = "student_base_info"
        table_description = "学生基本信息表"