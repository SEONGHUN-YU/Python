# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring

# Java의 XML파싱은 쫌 무식하게 한 줄씩 했었음(용량이 무지막지하게 크면 이 방식이 맞긴 함)
# jQuery의 XML파싱은 꽤나 세련됐었음, 전체 챙겨놓고 원하는 걸 찾아가는 스타일
# Python의 XML파싱은 jQuery에 가까운 스타일
huc = HTTPSConnection("www.kma.go.kr")
huc.request("GET", "/wid/queryDFSRSS.jsp?zone=1168064000")
resBody = huc.getresponse().read()
weatherXML = fromstring(resBody) # parsing할 수 있는 형태로 만듬 
                                # jQuery로 따지면 $(resBody) 느낌
weathers = weatherXML.getiterator("data")# <data></data>들(여러개) 찾을 때는 : .getiterator("")
                                                # ↑ $(resBody).find("data") 느낌 
for w in weathers: # 작정하고 줄이면 for문에 한 줄로 들어감
    # <hour></hour> 하나(데이터 하나) 찾을 때는 .find("").text
    print(w.find("hour").text)
    print(w.find("temp").text)
    print(w.find("wfKor").text)
huc.close()