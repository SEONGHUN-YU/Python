# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

# MongoDB : NoSQL -> JavaScript를 씀
#    테이블 -> 사실 JS의 배열[]이었다 -> Python에서는 list
#    데이터 -> 사실 JS의 객체{}였다 -> Python에서는 dict ?!
#    SQL    -> 사실 JS의 함수였다 -> Python 문법 ?!
# Node.js 가면 더 잘 맞아 떨어진다 함

# MongoDB제어할 때 썼던 문법 (거의)그대로 사용
try:
    con = MongoClient("192.168.0.152") # 서버랑 연결 시키고
    db = con.xe # con.db명(내가 use로 바꾼 거) <- 서버에 있는 DB에 연결
#   ↑ 이거랑 MongoDB 문법의 db랑은 상관 없는 거, 바뀌어도 된다는 소리
    n = input("품명 : "); p = int(input("가격 : "))
    
    data = {"p_name" : n, "p_price" : p}
    
    # 쌩MongoDB : db.테이블명.insertOne(JS객체)
    # pymongo   : db.테이블명.insert_one(dict)
    r = db.mar27_product.insert_one(data)
    if r.acknowledged == 1:
        print("성공")
except Exception as e:
    print(e)
con.close()