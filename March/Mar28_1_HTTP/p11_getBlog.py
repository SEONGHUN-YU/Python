# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient
from http.client import HTTPSConnection
from studykey import studykey
from urllib.parse import quote
from json import loads

def clean(s):
    s = s.replace("<b>", "").replace("</b>", "")
    s = s.replace("&lt;", "").replace("&gt;", "").replace("&#34;", "")
    return s

# 비정형 -> MongoDB
# title, contents, blogname
huc = HTTPSConnection('dapi.kakao.com')
huc.request('GET', '/v2/search/blog?query=' + quote(input('키워드 : '))
            , headers={"Authorization" : "KakaoAK " + studykey().Kakao()})
con = MongoClient('192.168.0.152')
db = con.xe
for oa in loads(huc.getresponse().read())['documents']:
    if db.daumBlog.insert_one({'title' : clean(oa['title'])
                               , 'contents' : clean(oa['contents'])
                               , 'blogname' : clean(oa['blogname']) }).acknowledged == 1:
        print('성공')
con.close()
huc.close()
