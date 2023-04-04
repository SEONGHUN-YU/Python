# -*- coding:utf-8 -*-

import numpy as np

a = np.random.randint(1, 11, 5)
b = np.random.randint(1, 11, 5)
print(a)
print(b)

c = np.intersect1d(a, b) # 교집합(양쪽 다 있는 거)
print(c)

d = np.union1d(a, b) # 합집합(중복 제외하고 전부 다)
print(d)

e = np.setdiff1d(a, b) # 차집합(a에서 b에 있는 거는 빼고)
print(e)

f = np.setxor1d(a, b) # 한쪽에만 있는 거(교집합의 반대 느낌)
print(f)

g = np.unique(a) # a에서 중복 제거
print(g)