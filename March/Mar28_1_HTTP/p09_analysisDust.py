# -*- coding:utf-8 -*-
from cx_Oracle import connect

# Python : hybrid한 객체지향 프로그래밍 언어[interpreter방식]
# Python : 분석툴

# 권역별, 미세+초미세의 평균
con = connect("databig/987654321@192.168.0.152:1521/xe")
sql = "select sd_MSRRGN_NM, avg(sd_PM10 + sd_PM25) from seoul_dust group by sd_MSRRGN_NM order by avg(sd_PM10 + sd_PM25) desc"
cur = con.cursor()
cur.execute(sql)
for city, avg in cur:
    print(city, avg)
cur.close()
con.close()