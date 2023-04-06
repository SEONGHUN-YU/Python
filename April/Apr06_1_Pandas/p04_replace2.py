# -*- coding:utf-8 -*-

import pandas as pd

a = pd.read_csv('D:/yu/titanic.csv')

# 이름, 성별빼고 나머지는 삭제
a = a[['Name', 'Sex']] # (엄밀히 따지면 삭제는 아니지만, 이름, 성별만 추출해온 것이랑 다를 바가 없음)

# male -> 남, female -> 여 로 바꾸기
a['Sex'] = a['Sex'].replace(['male', 'female'], ['남', '여'])
# a['Sex'] = a['Sex'].replace({'male' : '남', 'female' : '여'})

# Mr. -> 미스터
# a['Name'] = a['Name'].replace('Mr.', '미스터') # 정확하게 'Mr.'이 아니면 'aMr.'은 안 바뀜...
def func1(qwe):
    return qwe.replace('Mr.', '미스터')
a['Name'] = a['Name'].apply(func1)
print(a)
print('-----')

# 이름만 남게(성 제거)
# def func2(asd):
#     return asd.split(',')[0]
# a['Name'] = a['Name'].apply(func2)
a['Name'] = a['Name'].apply(lambda n : n.split(',')[0]) # 위의 func2를 lambda로 표현
print(a)
print('-----')
# lambda함수
def getSum(a, b):
    return a + b
print(getSum(10, 20)); print((lambda a, b : a + b)(10, 20))
print('-----')

b = pd.read_csv('D:/yu/titanic.csv')
b = b[['Name', 'Age', 'Survived']]
# 나이 -> 10대/20대/... 로
b['Age'] = b['Age'].fillna(900) # 나이가 없는 데이터는 채워놓기
b['Age'] = b['Age'].apply(lambda age:'%d0대' % (age // 10)) # / 로 나누면 float, // 로 나누면 int가 됨
b['Age'] = b['Age'].replace('900대', '없음')

# 나이대별로 사망자 수, 생존자 수
b = b.groupby(['Age', 'Survived'])['Age'].count()
print(b)