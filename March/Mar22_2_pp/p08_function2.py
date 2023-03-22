# -*- coding:utf-8 -*-
from setuptools.command.build_ext import if_dl

def getResult(a, b):
    c = a + b
    d = a - b
    e = a * b
    f = a / b
    g = a % b
    return (c, d, e, f, g)  # 착각하지말자, return이 여러개인 게 아니라 tuple 하나를 리턴하는 것

print(getResult(39, 10))
print("-----")

# 곱은 필요없는데?
z, x, _, v, _ = getResult(39, 10)  # _를 이용해서 값을 무시? 비슷하게 할 수 있음, tuple형태와 맞춰주지 않으면 에러
print(z, v)
# 생긴 것만 보면 Python은 return이 여러개 가능하다 : 엄밀히는 아님

# lambda함수
#    이름이 없음, 일회용 함수
# (lambda 파라메터1, 파라메터2, ... : 함수내용)(값1, 값2, ...)
# 함수내용 자리에 return은 생략
(lambda : print("사와"))()
(lambda a, b : print(a + b))(1, 2)
(lambda a, b, c : a + b + c)(1, 2, 3)
