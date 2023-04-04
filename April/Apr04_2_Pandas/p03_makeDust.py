# -*- coding:utf-8 -*-

# 실시간 서울시 미세먼지
# pd.DataFrame으로 한 번 출력해보자

from http.client import HTTPConnection
from studykey import studykey
from json import loads
import pandas as pd

huc = HTTPConnection("openapi.seoul.go.kr:8088")
huc.request("GET", "/" + studykey().Seoul() + "/json/RealtimeCityAir/1/25/")
dustDF = pd.DataFrame(loads(huc.getresponse().read())["RealtimeCityAir"]["row"]) # loads == JSON -> Python dict + list로 바꿔줌
dustDF = dustDF.set_index(dustDF['MSRSTE_NM']) # PK 같은 거 먹임, ~구로 찾겠다고 설정
print(dustDF.loc['중구']) # set_index 설정해줘야만 loc 가능
huc.close()