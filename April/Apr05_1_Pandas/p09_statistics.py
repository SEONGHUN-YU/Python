# -*- coding:utf-8 -*-

import pandas as pd

a = pd.read_csv('D:/yu/LNPS.csv', names=['시장이름', '품목', '가격', '시장종류', '구'])
print(a)
print('-----')

print(a.max()) # 모든 필드들 다 통계 냄
print(a['가격'].max()) # 특정 필드만 통계 내기
print(a['가격'].min())

print(a[a['가격'] == a['가격'].min()]) # 최소가 상품 정보
print(a['가격'].mean()) # 평균
print(a['가격'].median()) # 중앙값(평균하고는 좀 다름)
print(a['가격'].sum()) # 합계
print(a['가격'].count()) # 갯수
print(a['가격'].var()) # 분산
print(a['가격'].std()) # 표준편차
print(a['가격'].mode()) # 최빈값
print(a['가격'].describe()) # 알아서 통계 다 내라

print(a[a['가격'] == 3000])