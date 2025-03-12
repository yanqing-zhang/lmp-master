'''
@Project ：lmp-server-master 
@File    ：api_api.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/12 11:41 
'''
from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/list", summary="查看API列表")
async def list_api(
    page: int = Query(1, description="页码"),
    page_size: int = Query(10, description="每页数量"),
    path: str = Query(None, description="API路径"),
    summary: str = Query(None, description="API简介"),
    tags: str = Query(None, description="API模块"),
):
    pass


