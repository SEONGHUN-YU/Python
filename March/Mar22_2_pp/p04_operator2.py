# -*- coding:utf-8 -*-

name = input("이름 : "); height = float(input("키 : ")); age = int(input("나이 : "))
print("-----")

# 키가 height >= 150 이면 타는 거
# 나이가 age < 10 이면 타는 거

# 이름이 hong이면 타는 거
# Java에선 .equals()
# Python 글자가 같은지 비교 : ==
#     Java : String객체[실제 내용은 heap에]
#                    연산자는 stack이 대상
#     Python : 다 객체, 자료형을 사람이 신경 안 쓰도록
#            연산자가 뭐가 대상이고 그런 거 관심 없어함...

a = height >= 150; b = age < 10; c = name == 'hong'; print(a, b, c)

# && : and
# || : or
# ! : not

# 빅데이터하다가 &, | 하나만 쓰는 연산자를 써야만 할 경우가 올 것(나중에 배우자)

# 나이가 age >= 5 이고, 키가 height > 200 이면 타는 거
d = height > 200 and age >= 5; print(d) # 단축평가를 위해 height가 앞으로

# 20대만 타는 거 (age >= 20 and age < 30)도 가능하지만
e = 20 <= age <= 29; print(e) # <- 이 방식은 기억해둘 것 ★

# << 시프트연산자 건재함
# 삼항연산자 없는듯