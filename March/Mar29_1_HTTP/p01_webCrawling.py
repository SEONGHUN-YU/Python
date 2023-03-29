# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from bs4 import BeautifulSoup

# 분석용 데이터 구축
#    1.직접 기록
#    2.XML/JSON
#    3.완성된 csv같은 거 구해서
#    다 안되면 => 4.남의 웹사이트에서 가져올 수밖에 
#    HTML parsing(web crawling)
#    법적으로 문제 생길 수도(우리 기관에서는 data를 줄 생각이 없었는데 왜 가져가)
#    안 되게 막아놓은 사이트 많음
#    Front-end 기반으로 뭔가 추가되는 사이트
#        스크롤 하면 다음페이지 나오고... 이런 곳은 웹크롤링이 잘 안 됨
#    CSS선택자가 다양한 분야에 많이 쓰임
#    html/css : 웹개발 + 웹크롤링하기 위해

# Java : jsoup.jar
# Python : BeautifulSoup
# 시작 - cmd
#    pip install bs4

huc = HTTPSConnection("sdgn-djvemfu.tplinkdns.com")
huc.request("GET", "/")
                                            # html파서이름
bs = BeautifulSoup(huc.getresponse().read(), "html.parser", from_encoding="utf-8")
# ~~~.select("CSS선택자") -> list로 리턴
# ~~~.select_one("CSS선택자") -> 하나
# ~~~.text -> 내용
r = bs.select(".aSNSTxt2")
for s in r:
    print(s.text)
huc.close()
