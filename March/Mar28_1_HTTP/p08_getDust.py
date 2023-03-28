# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from studykey import studykey
from json import loads
from cx_Oracle import connect

# 언제, 권역, 구, 미세, 초미세, 상태
# MSRDT, MSRRGN_NM, MSRSTE_NM, PM10, PM25, IDEX_NM

huc = HTTPConnection("openapi.seoul.go.kr:8088")
huc.request("GET", "/" + studykey().Seoul() + "/json/RealtimeCityAir/1/25/")
con = connect("databig/987654321@192.168.0.152:1521/xe")
for oa in loads(huc.getresponse().read())["RealtimeCityAir"]["row"]: # {R{r[{},...]}}
    sql = "insert into seoul_dust values(sysdate, '%s', '%s', %d, %d, '%s')" % (oa['MSRRGN_NM'], oa['MSRSTE_NM'], oa['PM10'], oa['PM25'], oa['IDEX_NM'])
    cur = con.cursor()
    cur.execute(sql)
    cur.close()
con.commit()
con.close()
huc.close()
