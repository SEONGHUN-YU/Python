# -*- coding:utf-8 -*-
from cx_Oracle import connect

# 빅데이터 교육과정 : 책
#    kaggle이라는 대회가 있는데, 데이터를 줄테니 분석해보라고 던져주는 대회

# titanic.csv -> numpy/pandas -> 시각화하고 치우라 함
# 굳이 데이터 전체 다 가져와서 PC에서 (numpy + pandas)로 처리
# 실전형으로 DB에서 분석해서 가져오기

con = connect("databig/987654321@192.168.0.152:1521/xe")

# sql = "select * from kma_weather order by kw_hour" <- 굳이 다 가져온 거, 실전성 없긴 함
# sum = 0; count = 0; templist = []
# for d, h, t, w in cur:
#     sum += t; count += 1; templist.append(t)
# templist.sort(reverse=True)
# print(sum / count, templist[0])

sql = "select avg(kw_temp) from kma_weather" # <- 분석해서 가져옴
cur = con.cursor()
cur.execute(sql)
for avgTemp in cur:
    print(avgTemp[0])
cur.close()
print("-----")
sql =  "select kw_when, kw_hour from kma_weather where kw_temp = (select max(kw_temp) from kma_weather)"
cur = con.cursor()
cur.execute(sql)
for w, h in cur: # date : datetime객체 .month, .day 로 가져올 수 있다는 소리
    print("%d월 %d일 %d시" % (w.month, w.day, h))
cur.close()
con.close()

