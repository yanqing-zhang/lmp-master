'''
@Project ：lmp-server-master 
@File    ：response_wrapper.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/10 12:26 
'''
from typing import Any, Optional
from fastapi.responses import JSONResponse

class Success(JSONResponse):
    """
    用于返回成功信息,不带分页信息
    """
    def __init__(
        self,
        code: int = 200,
        msg: Optional[str] = "Ok",
        data: Optional[Any] = None,
        **kwargs,
    ):
        content = {"code": code, "msg": msg, "data": data}
        content.update(kwargs)
        super().__init__(content=content, status_code=code)

class Fail(JSONResponse):
    """
    用于返回错误信息
    """
    def __init__(
        self,
        code: int = 400,
        msg: Optional[str] = None,
        data: Optional[Any] = None,
        **kwargs,
    ):
        content = {"code": code, "msg": msg, "data": data}
        content.update(kwargs)
        super().__init__(content=content, status_code=code)

class SuccessExtra(JSONResponse):
    """
    用于返回带有分页信息的数据
    """
    def __init__(
            self,
            code: int = 200,
            msg: Optional[str] = None,
            data: Optional[Any] = None,
            total: int = 0,
            page: int = 1,
            page_size: int = 20,
            **kwargs,
    ):
        content = {
            "code": code,
            "msg": msg,
            "data": data,
            "total": total,
            "page": page,
            "page_size": page_size,
        }
        content.update(kwargs)
        super().__init__(content=content, status_code=code)