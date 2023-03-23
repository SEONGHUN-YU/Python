# -*- coding:utf-8 -*-
from random import randint

# Java
#   for : 반복횟수
#   for-each : 컬렉션 탐색용
#   while : 반복조건
#   do-while : 반복조건(최소 한 번은 보장되는)

# Python은 for-each랑 while밖에 없다
a = [123, 456, 789, 1234]
for i in a: # for (int i : a) {}
    print(i)
print("-----")

b = [0, 1, 2, 3, 4, 5]
for j in b:
    print(j)
print("-----")

for k in range(6): # range()라는 컬렉션을 써서, Java의 for문처럼 사용한 것
    print(k)
print("-----")
    
for q in range(1, 10, 3): # 1 ~ 9까지 3칸씩
    print(q)
print("-----")

b = ['ㅋㅋㅋ', 'ㅎㅎㅎ', 'ㅡㅡ', 'ㅇㅇ']
# enumerate(컬렉션)
#    (인덱스, 값) tuple로 줌
for w, e in enumerate(b):
    print(w, e)
# jQuery의 $.each : for + for-each 느낌 (인덱스, 객체)를 가졌었음
print("-----")

# dict[Java의 Map] : 순서개념 X, key-value
c = {"마우스":10000, "키보드":20000}
# dict객체.items()
#    (키, 값) tuple로 줌 <- But 순서는 지멋대로
for p, r in c.items():
    print(p, r)
print("-----")

# 1 ~ 10 사이의 랜덤한 숫자
# 9 나올 때까지 계속

# 기술을 본인한테 맞추나? No -> 본인이 기술에 적응해야지
# Python : 컨셉 자체가 메모리 효율적으로 쓰는 것에 관심이 없음
# x = 0 <- 괜히 이런 짓 하지말자, int를 byte로 쓰는 것처럼 어색하다
while True:
    x = randint(1, 10) # 1 ~ 10까지
    print(x)
    if x == 9:
        break # continue도 건재함