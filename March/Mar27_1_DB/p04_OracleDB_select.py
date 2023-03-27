# -*- coding:utf-8 -*-
from cx_Oracle import connect

# 연결
con = connect("databig/987654321@192.168.0.152:1521/xe")

# 데이터 확보(전체 조회 할 거라 필요 없음)

# SQL
sql = "select * from mar27_coffee order by c_name"

# 총괄매니저 겸 결과객체[PreparedStatement겸 ResultSet]
cur = con.cursor()

# 실행 -> 결과가 cur에 담김
cur.execute(sql)

for n, p in cur:
    print(n, p)
    print("-----")
cur.close()
con.close()