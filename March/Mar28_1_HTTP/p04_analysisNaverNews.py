# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

# 무슨 단어가 많이 언급되나 top

con = MongoClient("192.168.0.152")
db = con.xe
countDict = {}
for s in db.naverNews.find():
    for a in (s['제목'] + " " + s['내용']).split(" "):
        if a in countDict:
            countDict[a] += 1
        else:
            countDict[a] = 1
con.close()

class words:
    def __init__(self, word, count):            
        self.word = word
        self.count = count
            
tempList = [] # dict는 정렬개념이 없어서 정렬만을 위한 리스트
for key, value in countDict.items():
    tempList.append(words(key, value))
    
tempList.sort(key=lambda i:i.count, reverse=True)

for index, obj in enumerate(tempList):
    if index == 10:
        break
    print(obj.word, obj.count)