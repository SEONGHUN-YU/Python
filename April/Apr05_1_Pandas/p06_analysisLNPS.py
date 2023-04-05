# -*- coding:utf-8 -*-

import pandas as pd

a = pd.read_csv('D:/yu/LNPS.csv', names=['시장이름', '품목', '가격', '시장종류', '구'])

a = a.set_index(a['시장이름']) # 시장이름으로 찾을 수 있도록 설정
a = a.sort_index() # 시장이름 가나다순 정렬
print(a) # 전체출력
print('-----')

print(a.loc['통인시장']) # 통인시장것만 출력
print('-----')

print(a[a['시장이름'].str.contains('농협')]) # 농협시리즈만 출력
print('-----')

a = a.sort_values(by='가격', ascending=False) # 가격비싼순 정렬
print(a.head(10)) # 비싼거 top 10
print('-----')

a = a.sort_values(by=['구', '품목']) # 구별 -> 상품명별 정렬
print(a) # 정렬했으니 전체출력 해보기
print('-----')

# 함수 : 함수
# 메소드 : 객체의 행동 -> 객체가 있어야 행동을 하지

# print(a[a['품목'].isnull()]) # 값 없는 거 확인
a['품목'] = a['품목'].fillna('없음') # 값 없는 것들을 '없음'으로 채움
print(a[a['품목'].str.contains('사과')]['시장이름']) # 사과는 어떤 시장에 파나
# 값이 없는 게 있어서 출력이 안 됨 -> 채워서 해결함
print('-----')

# print(a[a['구'] == '강남구'])
for i in (a[a['구'] == '강남구']).index: # 강남구만 반복문 써서 보기 좋게 (음... 안 좋았던 예제)
    print(i)             # .iterrows(), .itertuples(), .values <- 이런 것도 있음, values는 () <- 안 붙임
print('-----')

print(a[a['가격'] >= 100000]) # 100000원 이상인 것만