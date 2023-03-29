# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

con = MongoClient("192.168.0.152")
db = con.xe
f = open("D:/yu/news.txt", "a", encoding="utf-8")
for n in db.news.find():
    f.write("%s\t%s\t" % (n['name'], n['txt']))
f.close()
con.close()

