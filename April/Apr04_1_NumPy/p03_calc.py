# -*- coding:utf-8 -*-

import numpy as np

# + - * / % 등등 연산자로 계산해도 되고
# function으로도 있긴 함

a = np.random.randint(1, 51, [2, 3])
b = np.random.randint(1, 51, [2, 3])
print(a)
print(b)

c = np.add(a, b) # a + b
print(c)

d = np.subtract(a, b) # a - b
print(d)

e = np.multiply(a, b) # a * b
print(e)

f = np.divide(a, b) # a / b
print(f)

g = np.mod(a, b) # a % b
print(g)

h = np.power(a, b) # **제곱
print(h)
print("----------")

# greater, greater_equal, less, less_equal, equal, not_equal 
i = np.greater(a, b) # a > b
print(i)
print("----------")

# 연습
name = np.array(['홍', '김', '이', '박', '최'])
# 키 : 150 ~ 190사이 랜덤한 거 5개
# 몸무게 : 50.0 ~ 100.0사이 랜덤한 거 5개
# 표준체중 = (키 - 100) * 0.9
# 비만도 = 체중 / 표준체중 * 100
# 비만도가 120초과하면 비만
# 비만인 사람의 이름 출력

height = np.random.randint(150, 191, 5)
weight = np.random.rand(5) * 50 + 50
# weight = np.random.rand(5) # 0.0 ~ 1.0
# weight = weight * 50       # 0.0 ~ 50.0
# weight = weight + 50       # 50.0 ~ 100.0

stdWeight = np.multiply(np.subtract(height, 100), 0.9) # (height - 100) * 0.9
obesity = (weight / stdWeight) * 100
obese = (obesity > 120)
print(name[obese])