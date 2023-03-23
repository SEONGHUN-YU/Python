# -*- coding:utf-8 -*-

class human:
    def __init__(self): # 생성자(constructor) : 객체가 만들어질 때
        print("사람객체 생성")
    
    def __del__(self): # 소멸자(destroyer) : 객체가 메모리상에서 없어질 때
        print("사람객체 없어짐")

# GarbageCollection : stack 영역은 자동으로 정리를 해주지만, 원래 메모리상의 heap영역은 사람이 직접 치워야 함
# ↑ heap영역 자동정리 시스템
# 그 자동이 언제 발동되는데? 더 이상 그 변수에 접근하지 못하게 되었을 때 실시간으로
# stack 영역은 프로그램이 종료되면 날아감(원래 자동)
h = human()
h2 = human()
h3 = h
print(id(h))
print(id(h2))
print(id(h3))

h = None
h3 = None

print('ㅋㅋㅋㅋㅋ')