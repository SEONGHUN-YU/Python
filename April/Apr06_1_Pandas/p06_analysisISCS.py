# -*- coding:utf-8 -*-

import pandas as pd

def convert(s):
    s = s.split(' ')
    if s[0] == '없음':
        return '없음'
    for ss in s:
        if ss.endswith('구'):
            return ss
        
a = pd.read_csv('D:/yu/ISCS.csv', names=['업종', '주소', '품목', '가격'])
a = a[a['가격'] > 0] # 0원짜리는 없애고 (추출을 안 하고)
a['주소'] = a['주소'].fillna('없음') # 없는 데이터가 있어서 대응, .replace(np.nan, '없음')도 가능
a['주소'] = a['주소'].apply(convert) # 주소 중에서, 구만 남기고
print(a.groupby('주소')['가격'].mean()) # 구별 평균가
print(a.groupby(['주소', '업종'])['가격'].mean()) # 구별 업종별 평균가
print(a.groupby(['업종', '주소'])['가격'].mean()) # 업종별 구별 평균가