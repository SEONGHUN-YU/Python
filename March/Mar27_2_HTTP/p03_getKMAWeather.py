# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring
from cx_Oracle import connect

# 오늘 것만 DB에 저장하는 프로그램
# 날짜, 시간, 기온, 날씨 -> day, hour, temp, wfKor
# 매일 아침마다 실행할 수 있도록

# 기능 확정 -> DB 설계 -> ...

huc = HTTPSConnection("www.kma.go.kr")
huc.request("GET", "/wid/queryDFSRSS.jsp?zone=1168064000")
con = connect("databig/987654321@192.168.0.152:1521/xe")
for w in fromstring(huc.getresponse().read()).getiterator("data"):
    if w.find("day").text == "1":
        break
    h = w.find("hour").text; t = w.find("temp").text; wfk = w.find("wfKor").text
    sql = "insert into kma_weather values(sysdate, %d, %s, '%s')" % (int(h), t, wfk)
    cur = con.cursor(); cur.execute(sql); cur.close()
con.commit()
con.close()
huc.close()