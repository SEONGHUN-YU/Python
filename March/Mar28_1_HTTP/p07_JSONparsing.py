# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from studykey import studykey
from json import loads

# JSON : JavaScript에서 객체쓰는 방식을 빌려서 데이터를 표현한 것
# JSON != JavaScript
#    JavaScript 배열 [] -> list
#    JavaScript 객체 {} -> dict

# JSON -> Python list + dict로 바꾸기
huc = HTTPConnection("openapi.seoul.go.kr:8088")
huc.request("GET", "/" + studykey().Seoul() + "/json/RealtimeCityAir/1/5/")
jp = loads(huc.getresponse().read()) # obj
jo = jp["RealtimeCityAir"]
ja = jo["row"]
for obj in ja:
    print(obj['MSRRGN_NM'])
huc.close()