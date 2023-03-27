# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

try:
    con = MongoClient("192.168.0.152")
    db = con.xe
    
    n = input("품명 : "); p = int(input("가격 : "))
    
    # 쌩MongoDB : db.테이블명.updateMany({찾을 거}, {바꿀 거});
    # pymongo   : db.mar27_product.update_many({찾을 거}, {바꿀 거})
    
    r = db.mar27_product.update_many({"p_name" : n}, {"$set" : {"p_price" : p}})
    if r.modified_count >= 1:
        print("성공")
except Exception as e:
    print(e)
con.close()
