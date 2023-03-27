# -*- coding:utf-8 -*-
from cx_Oracle import connect

try:
    # 연결
    con = connect("databig/987654321@192.168.0.152:1521/xe")
    
    # 데이터 확보
    n = input("이름 : "); p = int(input("가격 : "))
    
    # SQL(;만 빼고 완성시킴)
    sql = "insert into mar27_coffee values('%s', %d)" % (n, p)
    # Java 때 처럼
    #    ? -> 채우기 X, #{ } X
    
    # 총괄객체[Java의 PreparedStatement]겸 결과객체[ResultSet 느낌]임
    cur = con.cursor()

    # SQL을 서버로 전송, 실행 -> 결과가 cur에 담김 (약간 객체지향 뭉개진 느낌)
    cur.execute(sql)
    
    if cur.rowcount == 1:
        print("성공")
        con.commit()
        
except Exception as e:
    print(e)
cur.close()
con.close()