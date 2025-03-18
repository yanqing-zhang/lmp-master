'''
@Project ：jwt-sample 
@File    ：token_testcase.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/14 12:17 
'''
import requests

def test_raw_token():
    resp = requests.get("http://127.0.0.1:8000/protected_route")
    print(resp.status_code)
    print(resp.text)

    resp = requests.get("http://127.0.0.1:8000/protected_route", headers={"Token": "dev"})

    print(resp.status_code)
    print(resp.text)

def test_api_token():
    resp = requests.get("http://127.0.0.1:8000/protected_route")
    print(resp.status_code)
    print(resp.text)

    resp = requests.get("http://127.0.0.1:8000/protected_route", headers={"Token": "dev"})

    print(resp.status_code)
    print(resp.text)

if  __name__ == "__main__":
    # test_raw_token()
    test_api_token()