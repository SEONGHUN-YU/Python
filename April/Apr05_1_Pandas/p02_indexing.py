# -*- coding:utf-8 -*-

import pandas as pd

# indexing(조회)

a = pd.read_csv('D:/yu/titanic.csv')
print(a) # 전체조회
print('-----')
print(a.shape) # 몇행 몇열
print('-----')
print(a.columns) # 필드명들
print('-----')
# 어떻게 생겼는지 확인만 할 거면
print(a.head()) # 앞에서 몇 개만
print(a.tail()) # 뒤에서 몇 개만

print('열 기준-----')
print(a['Name']) # Name열만 확인
print('-----')
print(a.Age) # Age열만 확인
print('-----')
print(a[['Name', 'Age']]) # Name, Age 처럼 동시에 여러 열 확인하고 싶으면

print('행(데이터) 기준-----')
# 번호(순서) 기준으로 찾을 때 == iloc
print(a.iloc[0]) # 0번 데이터
print('-----')
print(a.iloc[0:5]) # 0 ~ (5 - 1)까지의 데이터
print('-----')
# index 기준으로 찾을 때 == loc
# 따로 index라는 걸 지정한 적이 없으면, index에 번호가 들어가 있긴 함
print(a.loc[0]) # 그래서 0번 데이터기는 한데
# index 설정 : 찾을 기준을 설정하기
a = a.set_index(a['Name']) # <- 이렇게하면 번호로 접근 못 함, 이것도 범위조회가 가능함
print(a)
print('-----')
print(a.loc['Dooley, Mr. Patrick']) # <- 이런 식으로 접근해야 함
print('-----')
print(a.loc['Montvila, Rev. Juozas' : 'Dooley, Mr. Patrick']) # 범위조회

print('행 + 열 기준-----') # 데이터를 찾아서 특정 필드만
print(a.loc['Dooley, Mr. Patrick']['Age']) # <- 방법1
print('-----')
print(a.loc['Dooley, Mr. Patrick','Age']) # <- 방법2

print('for문으로-----')
print(a.index)
print('-----')
for i in a.index:
    print(a.loc[i])
    
print('검색-----')
print(a['Age'] >= 30) # bool로 return
print('-----') # 여기도 masking 먹힘
print(a[a['Age'] >= 30])
print(a[(a['Age'] >= 20) & (a['Age'] <= 29)])