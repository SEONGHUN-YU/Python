# -*- coding:utf-8 -*-

import pandas as pd
from cx_Oracle import connect

a = pd.read_csv('D:/yu/titanic.csv')
print(a)

print('열 삭제-----') # 특정 필드를 지울 때
a = a.drop('PassengerId', axis=1)
a = a.drop(a.columns[0], axis=1)
a = a.drop(['Pclass', 'Name'], axis=1)
print(a)

print('행 삭제-----') # 특정 데이터(row)를 지울 때
a = a.set_index('Age')
a = a.drop(22.0) # index 기준
print(a)
print('-----')

# Pandas에서 삭제한다는 게 의미가 있나?
# 기본적으로 모든 작업이 원본을 안 건드는데
b = pd.read_csv('D:/yu/LNPS.csv', names=['시장이름', '품목', '가격', '시장종류', '구'])
print(b)

# 열 삭제 : 시장이름, 시장종류, 구 삭제
#            => 품목, 가격만 꺼내면 되는데??
b = b[['품목', '가격']]
print(b)

# 행 삭제 : 50000원 넘는 거 삭제
#            => 50000원 미만인 거만 masking으로 추출하면 되는데??
b = b[b['가격'] < 50000]
print(b)
print('-----')

con = connect('databig/987654321@192.168.0.152:1521/xe')
sql = 'select * from seoul_dust'
w = pd.read_sql(sql, con)

#   날짜      권역          구        미세    초미세    상태
# SD_WHEN SD_MSRRGN_NM SD_MSRSTE_NM  SD_PM10  SD_PM25 SD_IDEX_NM

# 도심권 데이터 삭제
w = w[w['SD_MSRRGN_NM'] != '도심권']
# 날짜, 권역, 상태 삭제
w = w[['SD_MSRSTE_NM', 'SD_PM10', 'SD_PM25']]
# 구별 미세+초미세 평균
w['TOTAL_PM'] = w['SD_PM10'] + w['SD_PM25']
w = w.groupby('SD_MSRSTE_NM')['TOTAL_PM'].mean()

con.close()