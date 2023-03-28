# -*- coding:utf-8 -*-
from cx_Oracle import connect
from idlelib.iomenu import encoding

# DB에 있는 거를 csv에 저장하기
# 3,28,12,18.0,맑음 (월,일,시,기온,날씨)

con = connect("databig/987654321@192.168.0.152:1521/xe")
sql = "select * from kma_weather"
f = open("D:/yu/kma.csv", "a", encoding="utf-8")
cur = con.cursor()
cur.execute(sql)
for d, h, t, w in cur:
    f.write("%d,%d,%d,%f,%s\n" % (d.month, d.day, h, t, w))
f.close()
cur.close()
con.close()

# 1) 분석 플랫폼중에는 DB에 접근 못하는 경우도 있음 : hadoop
#    그렇다보니 어쩔 수 없이 전체조회로 처리해야하는 경우도

# 2) 다른 과정에서는 DB모름
#   .csv만 분석, 장단에 맞추려면 우리도 DB데이터를 .csv로 만들어놔야 함
