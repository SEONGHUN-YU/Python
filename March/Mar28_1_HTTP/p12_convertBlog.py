# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

con = MongoClient("192.168.0.152")
db = con.xe
f = open("D:/yu/daumBlog.csv", "a", encoding="utf-8")
for d in db.daumBlog.find():
    f.write('%s\t%s\t%s\n' % (d['title'], d['contents'], d['blogname']))
f.close()
con.close()