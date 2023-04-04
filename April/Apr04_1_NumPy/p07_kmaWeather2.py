# -*- coding:utf-8 -*-

from cx_Oracle import connect

con = connect("databig/987654321@192.168.0.152:1521/xe")
sql = "select kw_hour, avg(kw_temp) from kma_weather group by kw_hour having avg(kw_temp) = (select max(avg(kw_temp)) from kma_weather group by kw_hour)"
cur = con.cursor()
cur.execute(sql)
for h, t in cur:
    print(h, t)
cur.close()
print("-----")

con = connect("databig/987654321@192.168.0.152:1521/xe")
sql = "select kw_hour, avg(kw_temp) from kma_weather group by kw_hour having avg(kw_temp) = (select min(avg(kw_temp)) from kma_weather group by kw_hour)"
cur = con.cursor()
cur.execute(sql)
for h, t in cur:
    print(h, t)
cur.close()
print("-----")

con = connect("databig/987654321@192.168.0.152:1521/xe")
sql = "select kw_hour, avg(kw_temp) from kma_weather group by kw_hour having avg(kw_temp) > (select avg(avg(kw_temp)) from kma_weather group by kw_hour) order by kw_hour"
cur = con.cursor()
cur.execute(sql)
for h, t in cur:
    print(h, t)
cur.close()
con.close()