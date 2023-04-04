# -*- coding:utf-8 -*-

import numpy as np

a = np.random.randint(1, 51, [2, 3])
print(a)

b = np.sum(a) # 총 합계 내기
print(b)

c = np.mean(a) # 평균 내기
print(c)

d = a - c # 각 값에서 평균 빼기
d = d ** 2 # 그걸 제곱
d = np.mean(d) # 한 것의 평균 == 분산
print(d)
d = np.sqrt(d) # 거기다 루트 씌움 == 표준편차
print(d)

e = np.var(a) # 분산(각 값들이 평균에서 얼마나 떨어져 있는지 보는 거)
print(e)

f = np.std(a) # 표준편차(각 값들이 평균에서 얼마나 떨어져 있는지 보는 거)
print(f)

g = np.max(a)
print(g)

h = np.min(a)
print(h)

i = np.max(a, axis=0) # 열방향
print(i)

j = np.mean(a, axis=1) # 행방향
print(j)

k = np.argmax(a) # 최댓값 어디(몇 번째)에 있는 지 index를 찾아주는 함수
print(k)

l = np.argmin(a) # 최솟값 어디(몇 번째)에 있는 지 index를 찾아주는 함수
print(l)

m = np.argmax(a, axis=0)
print(m)

n = np.argmin(a, axis=1)
print(n)

o = np.cumsum(a) # 누적합
print(o)

p = np.cumprod(a) # 누적곱
print(p)