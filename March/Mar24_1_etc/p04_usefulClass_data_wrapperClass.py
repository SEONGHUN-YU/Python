# -*- coding:utf-8 -*-

# Java
#   int a = 10;
#        10이 stack영역에 있음
#        프로그래밍 하다보면, 10이 heap영역에 있어야 하는 경우가 생김
#        String -> int로 바꿔야하는 상황
#   => 기본형 int말고 객체형 int가 필요
#   기본형에 해당하는 클래스 : wrapper class

# Python
#   기본형 같은 특징의 그런 건 없고, 다 객체 뿐
#   형변환은 무조건 생성자
s = "10"; i = int(s)

a = input("숫자(x, y, z, ... : ").split(","); k = 0
for i in a:
    try:
        k += int(i);
    except:
        pass
print(k)