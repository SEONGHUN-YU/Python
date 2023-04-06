# -*- coding:utf-8 -*-

import pandas as pd
from cx_Oracle import connect

a = pd.read_csv('D:/yu/titanic.csv')
print(a)

# Pclass에서 중복 없애고 다 보고 싶을 때(뭐뭐 있는지 확인할 때) 쓰면 좋음
print(a['Pclass'].unique())
print('-----')

# Pclass가 몇 종류인지 갯수가 알고싶을 때
print(a['Pclass'].nunique())
print('-----')

# Pclass가 각 등급별로 데이터가 몇 개씩 있는지 확인할 때
print(a['Pclass'].value_counts()) # 1등급 몇 개, 2등급 몇 개, ...
print('-----')

# 좌석클래스별 사망자 수, 생존자 수
print(a.groupby(['Pclass', 'Survived'])['PassengerId'].count())
print('-----')

# 좌석클래스별 가격 평균
print(a.groupby('Pclass')['Fare'].mean())
print('-----')

# 성별별 사망자 수, 생존자 수
print(a.groupby(['Sex', 'Survived'])['PassengerId'].count())
print('-----')

con = connect('databig/987654321@192.168.0.152:1521/xe')
sql = 'select * from kma_weather'
w = pd.read_sql(sql, con)
print(w['KW_WFKOR'].unique()) # 어떤 날씨가 있었는지
print(w['KW_WFKOR'].nunique()) # 몇 종류였는지 갯수
print(w['KW_WFKOR'].value_counts()) # 각 날씨별로 데이터 몇개인지
con.close()