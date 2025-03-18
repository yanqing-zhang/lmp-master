'''
@Project ：jwt-sample 
@File    ：password_sample_1.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/14 16:55 
'''
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

if __name__ == '__main__':
    print(get_password_hash("123456"))
