# -*- coding:utf-8 -*-

import numpy as np

a = np.random.randint(1, 51, [2, 3])
b = np.random.randint(1, 51, [2, 3])
print(a)
print(b)
c = np.maximum(a, b) # 각 항목들 중에 큰 것만 꺼내서 담음
print(c)
d = np.minimum(a, b) # 각 항목들 중에 작은 것만 꺼내서 담음
print(d)
print("----------")

x = np.random.rand(2, 3) * 10
print(x)
e = np.ceil(x) # 소수점 이하 올림(무조건 올려 버림)
print(e)
f = np.floor(x) # 소수점 이하 버림
print(f)
g = np.rint(x) # 소수점 이하 반올림
print(g)
h = np.round(x, 3) # 소수점 이하 3자리까지 나오는 반올림(4자리 째에서 반올림 시킴)
print(h)

i = np.ceil(x * 100) / 100  # 소수점 이하 3번째 자리에서 올림(0.345 -> 0.35)
print(i)                    # 특정위치의 올림 버림은 이런 식

y = np.random.randn(2, 3)
print(y)

j = np.abs(y) # 절댓값
print(j)       

k = np.sqrt(y) # 루트
print(k)

l = np.log(y) # 로그
print(l)

# pandas같은 후속기술들의 선수과목
# 그 후속기술들 중에는 (값이 없다/무한)을 표현 못하는 경우가 있음
z = np.array([23, 53, np.nan, np.inf, 123, 345])
print(z)

m = np.isnan(z)
print(m)

n = np.isinf(z)
print(n)
