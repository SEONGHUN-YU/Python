# -*- coding:utf-8 -*-
from cx_Oracle import connect

con = connect("databig/987654321@192.168.0.152:1521/xe")
p = int(input("가격 : "))
sql = "update mar27_coffee set c_price = c_price - %d where c_price = (select max(c_price) from mar27_coffee)" % p
cur = con.cursor()
cur.execute(sql)
if cur.rowcount >= 1:
    print("성공")
    con.commit()
cur.close()
con.close()