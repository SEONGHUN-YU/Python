# -*- coding:utf-8 -*-
from sympy.core.numbers import pi, Rational
from sympy.printing.pretty.pretty import pprint
import sympy
from sympy.core.symbol import symbols
from sympy.simplify.simplify import simplify
from sympy.core.function import expand, diff
from sympy.polys.polytools import cancel
from sympy.core.relational import Eq
from sympy.solvers.solvers import solve
from sympy.integrals.integrals import integrate

a = pi
print(a) 
pprint(a)  # 수식 형태로 출력(기호 같은?)
pprint(sympy.N(a))  # 기호시리즈 숫자로
print("-----")

b = Rational(1, 2)  # 분수
print(b)
pprint(b)
print("-----")

# 수학식을 쓸 건데 x,y를 수학식 속의 x,y라고 선언해주는 것
x, y = symbols("x y")
c = 2 * x + y ** 4
print(c)
pprint(c)
print("-----")

d = 3 * x ** 2 + 1
pprint(d)
dd = d.subs(x, 5)  # d식 속의 x에 5 넣어서 계산
pprint(dd)
print("-----")

e = 5 * x ** 3 + 7 * y ** 2 - 10
pprint(e)
ee = e.subs([[x, 2], [y, 3]]) # e식 속의 x에 2, y에 3 넣어서 계산
pprint(ee)
print("-----")

f = 3 * (x + 2) ** 2 + (x - 3) ** 3 + 12 + x * x
pprint(f)
f2 = simplify(f) # 식 정리
pprint(f2)
f3 = "3 * 2 + (x + 4) ** 4 - 13 - x"
f4 = simplify(f3) # 문자열로 된 식도 정리해줌
pprint(f4)
print("-----")

#sik = simplify(input('식 : ')).subs(x, float(input('x에 대입할 값 : ')))
# 예제
sik = input("식 : ")
x_val = float(input("x에 대입할 값 :"))
sik = simplify(sik)
ans = sik.subs(x, x_val)
pprint(sik)
pprint(ans)
print("-----")

g = (x - 3) * (x + 5)
pprint(g)
g2 = expand(g) # 식 전개
pprint(g2)
print("-----")

h = (2 * x ** 3 + 2) / (2 * x)
pprint(h)
h2 = cancel(h) # 약분
pprint(h2)
print("-----")

i = Eq(x * 3 + 1, 4) # 이 식이 4가 되려면 x값이 뭐여야 하는지 계산
pprint(i)
ii = solve(i) # 방정식 풀기
pprint(ii)
print("-----")

# 연립방정식
j1 = 2 * x + y ** 2 - 3
j2 = x + 10 + x ** 2 + y - 10
pprint(j1)
pprint(j2)
jj = solve([j1, j2])
pprint(jj)
print("-----")

k = 2 * x ** 4 + 3 * x ** 6
pprint(k)
# k2 = diff(k) # 미분
k2 = diff(k, x, 2) # k를 x에 관해서 2번하라
pprint(k2)
print("-----")

l = 2 * x ** 4 + 13
pprint(l)
l2 = integrate(l) # 적분
pprint(l2)
print("-----")


# 머신러닝 알고리즘이 어떤 식으로 돌아가는지 설명 듣고
# => lib을 만들려면 : 수학 잘해야 함

# 머신러닝 알고리즘이 잘 만들어져 있는 lib를 잘 쓰자 <- 이게 맞음
# => 수학 딱히... 필요없음 

# 컴퓨터 : 전자계산기
# 수학 라이브러리 : SymPy
# 설치 : pip install sympy
