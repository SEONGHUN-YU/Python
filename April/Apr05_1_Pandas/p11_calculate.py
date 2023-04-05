# -*- coding:utf-8 -*-

from http.client import HTTPConnection
from studykey import studykey
from json import loads
import pandas as pd

huc = HTTPConnection('openapi.seoul.go.kr:8088')
huc.request('GET', '/' + studykey().Seoul() + '/json/RealtimeCityAir/1/25/')
a = pd.DataFrame(loads(huc.getresponse().read())['RealtimeCityAir']['row'])
b = a[['MSRRGN_NM', 'MSRSTE_NM', 'PM10', 'PM25', 'IDEX_NM']] # MSRRGN_NM, MSRSTE_NM, PM10, PM25, IDEX_NM
                                                            # 권역, 구, 미세, 초미세, 상태
b = b.rename(columns={'MSRRGN_NM' : '권역', 'MSRSTE_NM' : '구', 'PM10' : '미세', 'PM25' : '초미세', 'IDEX_NM' : '상태'})
b['먼지'] = b['미세'] + b['초미세']
print(b['먼지'])
print('-----')

b = b.set_index(b['구']) # 구로 찾을 수 있게 설정
print(b.loc['강남구']) # 강남구 확인
print('-----')
b = b.sort_values(by='먼지', ascending=False) # 먼지 심한순으로 정렬
print(b) # 전체 확인
print('-----')
b['구'] = b['구'].replace('강남구', '학원') # 강남구 -> 학원
print(b[b['먼지'] > b['먼지'].mean()]) # 먼지가 평균보다 심한 것들

huc.close()