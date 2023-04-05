# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

a = pd.read_csv('D:/yu/mosquito.csv', names=['날짜', '물가', '집', '공원'])

# 값이 없는 게 아니고 None이라는 글자가 들어가 있음
# 있는 날 : 123.1
# 없는 날 : 'None'
# => Python이 자료형을 자동으로 정하는데 => object로 할 수 밖에...(str로 되어버림)
# => 'None'을 아예 없애자 #1
a['물가'] = a['물가'].replace('None', np.nan)
a['집'] = a['집'].replace('None', np.nan)
a['공원'] = a['공원'].replace('None', np.nan)

# 필드 자체 형변환 #2
# 글자 -> 숫자 : pd.to_numeric(바꿀 거) ★★★
# 숫자 -> 글자 : (바꿀 거).astype(str) ★★★
a['물가'] = pd.to_numeric(a['물가'])
a['집'] = pd.to_numeric(a['집'])
a['공원'] = pd.to_numeric(a['공원'])

# 결측치(측정이 안된 값) -> 평균값/최빈값 #3
a['물가'] = a['물가'].fillna(a['물가'].mean()) # 평균값
a['집'] = a['집'].fillna(a['집'].mode()[0]) # 최빈값
a['공원'] = a['공원'].fillna(a['공원'].mean())


a = a.set_index(a['날짜']) # 날짜로 찾을 수 있게 설정
print(a.loc['2021-05-08']) # 2021-05-08은 어땠는지
a['총합'] = a['물가'] + a['집'] + a['공원'] # 물가, 집, 공원 다 더해서
print(a[a['총합'] == a['총합'].max()]) # 최악인 날 정보
print(a[a['총합'] < a['총합'].mean()]) # 평균보다 모기가 덜 했던 날 정보