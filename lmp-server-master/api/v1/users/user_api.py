'''
@Project ：lmp-server-master 
@File    ：user_api.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/10 10:58 
'''
from fastapi import APIRouter, Query
from tortoise.expressions import Q
from mock.mock_login_json import menulist_admin_json, menulist_user_json
from utils.response_wrapper import Success, Fail
router = APIRouter()

from core.dependence import AuthControl
from mock.mock_login_json import create_user,mock_user_list
from models.permission import LoginUser
@router.get("/list", summary="查看用户列表")
def list_user(
        page: int = Query(1, description="页码"),
        page_size: int = Query(10, description="每页数量"),
        username: str = Query("", description="用户名称，用于搜索"),
        email: str = Query("", description="邮箱地址"),
        phone_no: str = Query("", description="手机号"),
        dept_id: int = Query(None, description="部门ID"),
    ):
    q = Q()

    return "list_user"


@router.get("/get", summary="查看某用户")
def get_user(
        user_id: int = Query(..., description="用户ID"),
):

    return "get_user"

