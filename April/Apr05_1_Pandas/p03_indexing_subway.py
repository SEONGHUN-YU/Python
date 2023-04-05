# -*- coding:utf-8 -*-

import pandas as pd

# 지하철 csv
a = pd.read_csv('D:/yu/subway.csv', names=['년', '월', '일', '노선', '역', '타', '내'])

print(a.columns) # 필드명
print('-----')
print(a.head(3)) # 첫 3개
print('-----')
print(a.iloc[10:16][['노선', '역']]) # 10 ~ 15번까지 노선번호, 역명
print('-----')
a = a.set_index(a['노선']) # 노선번호로 찾도록 설정
# print(a[a['노선'] == '2호선']) # 2호선 전부
print(a.loc['2호선'])
print('-----')
# print(a[(a['노선'] == '3호선') & [['역', '타', '내']]]) # 3호선 역명, 탄 사람, 내린 사람
print(a.loc['3호선'][['역', '타', '내']])
print('-----')
print(a[a['타'] >= 50000]) # 탄 사람이 50000명 이상인 데이터 조회
print('-----')
print(a[(a['내'] < 10000) & [['년', '월', '일', '역', '내']]]) # 내린 사람이 10000명 미만인 데이터 년, 월, 일, 역명, 내린 사람
print('-----')
print(a[a['역'] == '서울역']) # 서울역 전부
print('-----')
print(a[a['역'].str.contains('서울')]) # '서울'이 들어가는 역 전부(SQL의 like 같은 느낌)
                # .startswith(), .endswith()도 있음
print(a[a['역'].str.endswith('입구')][['역', '타', '내']]) # '입구'로 끝나는 역 역명, 탄 사람, 내린 사람 