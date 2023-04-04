# -*- coding:utf-8 -*-

import pandas as pd
from cx_Oracle import connect
from pymongo.mongo_client import MongoClient

# titanic.csv(첫 줄에 제목(names가 될만한 거)이 있음)
a = pd.read_csv("D:/yu/titanic.csv")
print(a)

# subway.csv(첫 줄에 제목(names가 될만한 거)이 없음)
b = pd.read_csv("D:/yu/subway.csv", names=["년", "월", "일", "노선", "역", "타", "내"])
print(b)

# 다른 파일, 다 필요없고 read_csv
c = pd.read_csv("D:/yu/daumBlog.txt", sep="\t", names=["제목", "내용", "블로그명"])
print(c)

# OracleDB
con = connect("databig/987654321@192.168.0.152:1521/xe")
sql = "select * from kma_weather"
d = pd.read_sql(sql, con)
print(d)

# 전체를 가져와서 -> pandas로 하는 게 맞는가...
# sql로 다 해서 가져오는 게 맞는가 <- 이게 최고긴한데...
# 시간대별로 평균내서, 평균기온보다 높은 시간대, 시간대 오름차순 정렬 pd.DataFrame으로
con = connect("databig/987654321@192.168.0.152:1521/xe")
sql = "select kw_hour, avg(kw_temp) from kma_weather group by kw_hour having avg(kw_temp) > (select avg(avg(kw_temp)) from kma_weather group by kw_hour) order by kw_hour"
e = pd.read_sql(sql, con)
print(e)
con.close()

# MongoDB
# RDB(관계형DB) : 공통적으로 SQL로 제어
# NoSQL : 각자 다 따로 SQL 안 씀
#    MongoDB - JavaScript(JSON형태라서 바로 가능)
con2 = MongoClient("192.168.0.152")
db = con2.xe
f = pd.DataFrame(db.daumBlog.find())
print(f)
con2.close()

# 앞으로 우리는 DB에 있는 거 바로 pd.DataFrame으로 만들던지 or
# Hadoop에서 전처리 해온 거를 pd.DataFrame으로 만들던지