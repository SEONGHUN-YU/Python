# -*- coding:utf-8 -*-

# 접근제한자, method type도 없고, 리턴타입도 안 써도 됨

# 1) 함수정의
# def 함수명(변수명[=기본값], 변수명[=기본값], ...):
#     내용
# 들여쓰기로 스코프 구분
def yaDambae():
    print("어머니께 돈 받아서")
    print("슈퍼 가서...")
    
def printHab(a=1, b=2): # parameter에 기본값 넣어두는 게 가능함
    print("-----")
    print(a)
    print(b)
    print(a + b)

# 개발중이라는 컨셉 -> 함수 내용에 넣을 게 없는데? 근데 안 쓰면 안 되고...
def test():  
    pass # 함수의 콜론(:) 뒤에는 들여쓰기가 있어야 하니, 그냥 자리만 차지시키는 용도, 에러방지용이라고 보면 됨

def getHab(c=1, d=1):
    return c + d

# 2) 호출 (interpreter방식에 main이 어딨어, 그냥 호출만), JS와 다르게 호이스팅이 없네
yaDambae()
printHab(20, 30) # 기본적으로는 순서가 있지만
printHab(b=200, a=300) # 특정 parameter에 값 넣는 게 가능함, 순서도 상관 없음
printHab(b=900)
printHab() # 기본값으로 실행됨
print("1", end="abc\n") # 이게 특정 parameter에 값 넣는 것의 예시라고 볼 수 있음

print(getHab())
print(getHab(30, 50))
print(getHab(d=100))

# overloading이 없음 (호출할 때 구별이 안 돼서 <- 기본값 넣어두는 시스템 때문에 혼란이 생길 수 있음)