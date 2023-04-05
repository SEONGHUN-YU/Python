# -*- coding:utf-8 -*-

import pandas as pd

a = pd.read_csv('D:/yu/titanic.csv')
print(a)
a = a.set_index(a['Name']) # 사람 이름으로 찾도록 설정

print('index기준-----')
a = a.sort_index() # 오름차순 정렬
print(a)
print('-----')
a = a.sort_index(ascending=False) # 내림차순 정렬
print(a)

print('행 방향 정렬-----')
a = a.sort_index(axis=1) # 필드명 순서 바꾼 거(크게 의미는 없음)
print(a)                 # 마찬가지로 ascending=False 가능 

print('데이터 정렬-----')
a = a.sort_values(by='Survived') # 생사여부로 정렬
print(a[['Pclass', 'Survived']]) # 생략돼서 어쩔 수 없이 이렇게 조회함, 문법 아님
print('-----')
a = a.sort_values(by=['Pclass', 'Survived']) # 좌석등급 -> 생사여부로 정렬
print(a[['Pclass', 'Survived']])
print('-----')
a = a.sort_values(by=['Age', 'Fare'], ascending=[False, True]) # 나이 많은 순 -> 요금 적은 순
print(a[['Age', 'Fare']])

# 정렬을 하면 디폴트로 항상 오름차순으로 되어 있음