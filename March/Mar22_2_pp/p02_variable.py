# -*- coding:utf-8 -*-

# Java보다 고급언어
# 저급언어 : 개발자가 직접 컨트롤
# 고급언어 : 언어 자체적으로 자동으로 처리

# Java에서는 적절한 자료형 선택하기가 필요했는데 Python은 자료형 안 쓰고 선언해도 됨
# Python에서는 클래스명 첫글자를 대문자로 해야하는 불문율 그런 거 없음
# Python은 기본형 없고 다 객체임(참조형)

a = 0
for i in range(11):
    a = i
# ↑ 이런 게 혼란스러움 a라는 식별자를 만드는 건지 값만 바꾸는 건지
# 자료형 확인은 type(), heap영역 주소값 확인은 id()
# 쉼표연산자 있음
print(type(a), id(a))

b = 10
print(b, type(b), id(b))
b = "hi"
print(b, type(b), id(b))
print(a == b)

# Java 정수 : byte, short, int, long이 있었는데
# Python에서는 -> 그냥 int객체

# Java 실수 : float, double
# Python에서는 -> 그냥 float객체

# Java 문자 : char[1글자일 때], String[여러글자일 때]
# Python에서는 -> 그냥 str객체

# Java 논리 : boolean
# Python에서는 -> 그냥 bool객체
# Java에서는 소문자였는데 Python에서는 True, False처럼 첫글자를 대문자로 쓴다