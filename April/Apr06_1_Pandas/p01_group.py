# -*- coding:utf-8 -*-

import pandas as pd
from cx_Oracle import connect

a = pd.read_csv('D:/yu/LNPS.csv', names=['시장이름', '품목', '가격', '시장종류', '구'])
print(a)
print('-----')

print(a['가격'].mean())
print('-----')

# 시장종류별 가격 평균
print(a.groupby('시장종류')['가격'].mean())
print('-----')

# 구별 시장종류별 가격 평균 (일단 구별로 묶고, 거기서 또 시장종류별로 묶는다)
print(a.groupby(['구', '시장종류'])['가격'].mean())
print('-----')

# 날씨별 평균기온
con = connect('databig/987654321@192.168.0.152:1521/xe')
sql = 'select * from kma_weather'
w = pd.read_sql(sql, con)
print(w.groupby('KW_WFKOR')['KW_TEMP'].mean())
con.close()