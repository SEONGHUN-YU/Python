# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

try:
    con = MongoClient("192.168.0.152")
    db = con.xe
    
    for p in db.mar27_product.find({"p_name" : {"$regex" : "1"}}):
        print(p["p_name"], p["p_price"])
except Exception as e:
    print(e)
con.close()
    