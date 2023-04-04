# -*- coding:utf-8 -*- 
import numpy as np

a = np.random.randint(1, 101, [3, 5])
b = np.random.randint(1, 101, [3, 5])
print(a)
print(b)
print("-----")

ab = np.concatenate([a, b]) # 붙이기(a뒤에다 b를 붙임)
print(ab)
print("-----")

ab2 = np.append(a, b) # 붙여서(a뒤에다 b를 붙여서) 1차원으로
print(ab2)
print("-----")

# axis=0 : 열방향
# axis=1 : 행방향            axis=0이 기본값
ab3 = np.concatenate([a, b], axis=1) # a[0]뒤에 b[0]붙이고...
print(ab3)
print("-----")
                        # 기본값이 따로 있지 않음
ab4 = np.append(a, b, axis=0) # ab랑 같아짐
print(ab4)
print("-----")

ab5 = np.append(a, b, axis=1) # ab3랑 같아짐
print(ab5)
print("--------------------")

a2 = np.array_split(a, 2) # a를 2개로 나누기(대충 나눔)
print(a2)

a3 = np.split(a, 3) # a를 3개로 똑같이 나누기(똑같이 나눌 수 없으면 Error)
print(a3)
