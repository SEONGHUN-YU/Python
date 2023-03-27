# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient
from pymongo import DESCENDING, ASCENDING

# MongoDB
#    테이블 -> 데이터, 의 조합 X
#    [] -> {}, 의 조합 O
#    => Python list + dict

try:
    con = MongoClient("192.168.0.152") # 서버랑 연결
    db = con.xe # db랑 연결
    
    # 쌩MongoDB : db.테이블명.find()
    # pymongo   : db.테이블명.find()
    
    # 정렬(비정형데이터 10억개 정렬해서 뭐하게...)
    # .sort([조건1, 조건2,...])
    # 각각의 조건 하나하나는 tuple 형태로 써야 함
    # .sort([("필드명", ASCENDING), ("필드명", ...)] <- 이런 식
    
    # 전체, 가격 높은 순 -> 이름 가나다 순
    for p in db.mar27_product.find().sort(
        [("p_price", DESCENDING), ("p_name", ASCENDING)]): # [{},{},{}] 순회
        print(p['p_name'])
        print(p['p_price'])
        print("-----")
except Exception as e:
    print(e)
con.close()