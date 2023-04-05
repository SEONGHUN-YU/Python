# -*- coding:utf-8 -*-

import pandas as pd
from cx_Oracle import connect

con = connect('databig/987654321@192.168.0.152:1521/xe')
sql = 'select * from kma_weather'
w = pd.read_sql(sql, con)
print(w)
print(w['KW_TEMP'].mean()) # 평균기온
print(w['KW_TEMP'].max()) # 최고기온
print(w[w['KW_TEMP'] == w['KW_TEMP'].max()]) # 기온이 최고기온이었던 거
print(w[w['KW_TEMP'] > w['KW_TEMP'].mean()]) # 평균기온보다 높았던 거
con.close()