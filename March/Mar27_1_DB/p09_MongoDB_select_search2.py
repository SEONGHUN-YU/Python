# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

try:
    con = MongoClient("192.168.0.152")
    db = con.xe
    
    min = int(input("최저가 : ")); max = int(input("최고가 : "))
    
    # 쌩MongoDB : db.테이블명.find({연산자 : [{조건1}, {조건2}, ...]});
    # pymongo   : 완전히 같음
    for p in  db.mar27_product.find({"$and" : [{"p_price" : {"$gte" : min}}, {"p_price" : {"$lte" : max}}]}):
        print(p["p_name"], p["p_price"])
        
    # RDB : 테이블을 나눠서 디자인하고, 관계를 중심으로 풀어나감
    # NoSQL : 한데 뭉쳐서
    
    # subquery : SQL에는 변수가 없음, MongoDB는 JS라서 변수 사용 가능
    # join도 없다
except Exception as e:
    print(e)
con.close()