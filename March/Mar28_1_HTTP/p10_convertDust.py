# -*- coding:utf-8 -*-
from cx_Oracle import connect
from datetime import datetime

# 월, 일, 시, 권역, 구, pm10, pm25, 상태
con = connect("databig/987654321@192.168.0.152:1521/xe")
sql = "select * from seoul_dust order by sd_when"
f = open("D:/yu/dust_py.csv", "a", encoding="utf-8")
for date, area, city, pm10, pm25, condition in con.cursor().execute(sql):
    f.write("%s,%s,%s,%.1f,%.1f,%s\n" % (datetime.strftime(date, "%m,%d,%H"), area, city
                                               , pm10, pm25, condition))
# date.month, date.day, date.hour도 가능한데 굳이 datetime.strftime을 써보았다
f.close()
con.close()
