# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from urllib.parse import quote
from xml.etree.ElementTree import fromstring
from pymongo.mongo_client import MongoClient
from studykey import studykey

def clean(s):
    s = s.replace("<b>", "").replace("</b>", "")
    s = s.replace("&apos;", "").replace("&quot;", "").replace("&amp;", "")
    return s

# VITQwGJ87taKzIBU1ALt
# dCQNImVfMu

# Python에서 ㅋ -> %2A
# 인터넷 주소는 한글 못 씀, URL인코딩 해줘야 함 quote() 사용
# q = quote("코로나") # <- 이런 식
huc = HTTPSConnection("openapi.naver.com")
huc.request("GET", "/v1/search/news.xml?query=" + quote(input("키워드 : ")),
            headers={"X-Naver-Client-Id" : studykey().Id(),
                     "X-Naver-Client-Secret" : studykey().Secret()})
            # headers라는 parameter에 dict 형식으로 넣어준다
con = MongoClient("192.168.0.152")
db = con.xe
for s in fromstring(huc.getresponse().read()).getiterator("item"):
    r = db.naverNews.insert_one({"제목" : clean(s.find("title").text),
                                 "내용" : clean(s.find("description").text)})
    if r.acknowledged == 1:
        print("성공")
con.close()
huc.close()