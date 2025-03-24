'''
@Project ：tortoise-orm-samples 
@File    ：utils.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/24 17:04 
'''
from datetime import date, time

def model_to_dict(instance, include=None):
    """将模型实例转换为字典，支持过滤字段和日期时间格式化"""
    fields = {}
    for field in instance._meta.fields_map.keys():
        if include and field not in include:
            continue
        value = getattr(instance, field)
        if isinstance(value, (date, time)):  # 检查是否为日期或时间类型
            value = value.isoformat()  # 转换为 ISO 格式字符串
        fields[field] = value
    return fields

def model_to_dict_with_exclude(instance, exclude=None):
    """将模型实例转换为字典，支持过滤字段和日期时间格式化"""
    fields = {}
    for field in instance._meta.fields_map.keys():
        if exclude and field in exclude:
            continue
        value = getattr(instance, field)
        if isinstance(value, (date, time)):  # 检查是否为日期或时间类型
            value = value.isoformat()  # 转换为 ISO 格式字符串
        fields[field] = value
        formatted_string = ','.join(f'{key}="{value}"' if isinstance(value, str) else f'{key}={value:.3f}' for key, value in fields.items())
    return formatted_string