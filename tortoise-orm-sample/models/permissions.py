'''
@Project ：tortoise-orm-samples 
@File    ：permissions.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/24 9:36 
'''
from tortoise import fields
from tortoise.models import Model

class  User(Model):
    id = fields.IntField(primary_key=True, description="主键自增")
    user_id = fields.CharField(max_length=50, description="用户编号")
    user_name = fields.CharField(max_length=100, description="用户姓名")
    avatar_url = fields.CharField(max_length=500, description="头像地址URL")
    login_name = fields.CharField(max_length=100, description="登录账号")
    login_password = fields.CharField(max_length=50, description="登录密码")
    latest_login_at = fields.DatetimeField(description="最近一次登录时间", auto_now=True)
    gender = fields.IntField(description="性别")
    phone_no = fields.CharField(max_length=20, description="手机号")
    email = fields.CharField(max_length=50, description="电邮")
    wechat_id = fields.CharField(max_length=100, description="微信号")
    create_user_id = fields.CharField(max_length=50, description="创建人编号")
    update_user_id = fields.CharField(max_length=50, description="修改人编号")
    create_at = fields.DatetimeField(description="创建时间", auto_now_add=True)
    update_at = fields.DatetimeField(description="修改时间", auto_now=True)
    yn = fields.IntField(description="此条数据是否可用,0为软删除，1正常", default=1)

    class Meta:
        table = "users"