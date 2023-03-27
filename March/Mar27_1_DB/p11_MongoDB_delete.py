# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

try:
    con = MongoClient("192.168.0.152")
    db = con.xe
    
    n = input("품명 : ")
    
    # NoSQL의 대표로 MongoDB를 배웠는데
    # 서버급 컴퓨터 여러대에 병렬 저장, 조회...
    # elasticsearch <- 비정형 데이터를 이쪽으로 처리하는 걸 해보자
    
    # 분석용데이터구축
    # 서버급 컴퓨터 여러대로 병렬 전처리가 필요 : hadoop
    # numpy, pandas
    
    # 정형 : OracleDB에 넣는다
    # 비정형 : MongoDB에 넣는다
    
    # 쌩MongoDB : db.테이블명.deleteMany({찾을 조건});
    # pymongo   : db.테이블명.delete_many({찾을 조건})
    
    r = db.mar27_product.delete_many({"p_name" : {"$regex" : n}})
    if r.deleted_count >= 1:
        print("성공")
except Exception as e:
    print(e)
con.close()