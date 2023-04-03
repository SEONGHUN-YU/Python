# -*- coding:utf-8 -*-
import numpy as np
a = [10, 20]
b = [1, 2]
c = a + b # 기존 list는 append가 됨
print(c)
print("----------")

aa = np.array([10, 20])
bb = np.array([1, 2])
cc = aa + bb # (1x2) + (1x2)
print(cc)    # 모양이(차원수가) 같으면 같은 자리끼리 계산됨
dd = aa * bb # 마찬가지로 같은 자리끼리 계산됨
print(dd)
ee = aa * 5 # (1x2) + (1)
print(ee)   # broadcasting
            # 차원수가 다르면 작은 거를 큰 쪽에 맞춰서 항목별로 계산됨
print("----------")

name = np.array(["홍길동", "김길동", "최길동"])
kor = np.array([100, 90, 20])
eng = np.array([10, 70, 30])
mat = np.array([50, 50, 10])

# 각 학생의 평균점수
sum = kor + eng + mat # 셋 다 (1x3)
avg = sum / 3         # (1x3) / (1) : broadcasting
print(avg)

over40 = avg > 40
print(over40)

# masking <- 차원수가 전부 같을 때에만 편리하게 해줌
print(name[over40]) # True인 index에 해당하는 값만 나오게 해줌
# 국어점수가 90점 이상인 학생 이름만 나오게
print(name[kor >= 90])
# 30 < 수학점수 < 60인 학생
# print(name[30 < mat < 60]) <- 이거 안 됨
print(name[(mat > 30) & (mat < 60)]) # 중간에 끊기지 않기 위해 &사용, 소괄호 필요
# &&(and) : 더 볼필요 없으면 중간에 끊는
# & : 무식하게 끝까지 함
# => 지금은 중간에 끊기면 애매(연산을 일일히 하나씩 다 해봄)