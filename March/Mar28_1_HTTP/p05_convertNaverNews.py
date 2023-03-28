# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

# 웹상의 실시간데이터를 내 DB에 적재해두는 red
# 내 DB에 적재되어있을 데이터를 분석용 파일로 만드는 blue

con = MongoClient("192.168.0.152")
db = con.xe
f = open("D:/yu/naverNews.txt", "a", encoding="utf-8")
for i in db.naverNews.find():
    f.write("%s\t%s\n" % (i['제목'], i['내용']))
f.close()
con.close()
