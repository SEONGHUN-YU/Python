# -*- coding:utf-8 -*-
from studykey import studykey
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

# http://openapi.seoul.go.kr:8088/+ key +/xml/CardSubwayStatsNew/1/5/20151101
# 2015/1/1 ~ 2022/12/31 지하철 운행정보 subway.csv로 저장하는 프로그램
# 년,월,일,호선,역이름,타고,내리고

def parsing(a, b, c, d, e):
    return "%s,%s,%s,%s,%s\n" % ("%s,%s,%s" % (a[0:4], a[4:6], a[6:8]), b, c, d, e)

# USE_DT, LINE_NUM, SUB_STA_NM, RIDE_PASGR_NUM, ALIGHT_PASGR_NUM
huc = HTTPConnection("openapi.seoul.go.kr:8088")
f = open("D:/yu/subway_py.csv", "a", encoding="utf-8")
for y in range(2015, 2023):
    for m in range(1, 13):
        for d in range(1, 32):
            huc.request("GET", "/" + studykey().Seoul() +
                        "/xml/CardSubwayStatsNew/1/610/" + "%d%02d%02d" % (y, m, d))
            for s in fromstring(huc.getresponse().read()).getiterator("row"):
                f.write(parsing(s.find("USE_DT").text, s.find("LINE_NUM").text,
                                s.find("SUB_STA_NM").text.replace(",", " "),
                                s.find("RIDE_PASGR_NUM").text, s.find("ALIGHT_PASGR_NUM").text))
f.close()
huc.close()