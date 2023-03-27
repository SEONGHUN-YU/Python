# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

# Python + OracleDB : cx_Oracle.py <- 정형데이터에 유리한 조합
# Python + MongoDB  : pymongo.py <- 비정형데이터에 유리한 조합
# pymongo 설치
#   시작 - cmd
#       pip install pymongo

try:
    con = MongoClient("192.168.0.152") # 서버의 ip주소
    print(con)
except Exception as e:
    print(e)
con.close()