# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from bs4 import BeautifulSoup
from pymongo.mongo_client import MongoClient

# 신문사, 제목
huc = HTTPSConnection("news.naver.com")
huc.request("GET", "/main/ranking/popularDay.naver")
con = MongoClient("192.168.0.152")
db = con.xe
for n in BeautifulSoup(huc.getresponse().read(), "html.parser", from_encoding="utf-8").select(".rankingnews_box"):
    name = n.select_one(".rankingnews_name").text # 신문사
    for k in n.select(".list_content a"): # 제목
        txt = k.text
        if db.news.insert_one({"name" : name, "txt" : txt}).acknowledged == 1:
            print("성공")
con.close()
huc.close()