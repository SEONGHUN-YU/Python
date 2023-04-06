# -*- coding:utf-8 -*-

import pandas as pd

a = pd.read_csv('D:/yu/titanic.csv')
b = pd.read_csv('D:/yu/titanic.csv')

ab = pd.concat([a, b]) # a뒤에 b가 붙음 (데이터 추가, column이 아래로 늘어남)
print(ab)
print('-----')

ab2 = pd.concat([a, b], axis=1) # a옆에 b가 (필드 추가, row가 옆으로 늘어남)
print(ab2)

snackDF = pd.DataFrame()
snackDF['이름'] = ['초코파이', '새우깡']
snackDF['가격'] = [5000, 3000]
snackDF['제조사'] = ['오리온', '농심']

companyDF = pd.DataFrame(
    {
        '제조사' : ['오리온', '농심', '롯데'],
        '위치' : ['서울', '인천', '부산']
    }
)

cityDF = pd.DataFrame(
    [
        {'도시' : '서울', '인구' : 200},
        {'도시' : '인천', '인구' : 100}
    ]
)

# snackDF에도 제조사, companyDF에도 제조사 -> 같은 게 있음
# 같은 필드가 있으면 알아서 -> inner join
snackCompanyDF = pd.merge(snackDF, companyDF, on='제조사') # 같은 필드가 여러개라면? on='기준으로 삼을 필드명'(1개만 가능)
print(snackCompanyDF)
print('-----')

snackCompanyDF = pd.merge(snackDF, companyDF, on='제조사', how='outer') # outer join 하고 싶으면 how='outer'
print(snackCompanyDF)
print('-----')

companyCityDF = pd.merge(companyDF, cityDF, left_on='위치', right_on='도시') # 필드명이 다르면 left_on='', right_on=''
print(companyCityDF)
print('-----')

# 인구수 제일 많은 도시에서 만들어진 과자 평균가
# RDB
#    join : 하면 할 수록 데이터 수가 폭증(필요하지 않은 정보까지 다 붙어서) -> 필터링
#    subquery : 하면 할 수록 데이터 수를 줄임(쓸데없는 정보를 줄여가며 찾으니)
#        너무 복잡함
#        메모리 신경쓸 거면 애초에 Python 안 하는 게 맞음
# subquery style : 연관된 거 값 찾아서...
w = cityDF['인구'].max() #1
x = cityDF[cityDF['인구'] == w]['도시'].iloc[0] #2
y = companyDF[companyDF['위치'] == x]['제조사'].iloc[0] #3
z = snackDF[snackDF['제조사'] == y]['가격'].mean() # 4
print(z)
print('-----')

# join style : 일단 붙여놓고...
joinStyle = pd.merge(pd.merge(snackDF, companyDF), cityDF, left_on='위치', right_on='도시')
print(joinStyle[joinStyle['인구'] == joinStyle['인구'].max()]['가격'].mean())
