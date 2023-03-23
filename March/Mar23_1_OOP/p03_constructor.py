# -*- coding:utf-8 -*-

def test(a=10, b=20):
    pass
# 호출 때 parameter로 구별불가 -> overloading 불가능
test() # 기본값 시스템
test(b=30) # 원하는 인자만 넣는 시스템
test(30, 50) # 원래 작동 시스템

# Python은
#    외부에서 멤버변수 추가 가능 <- 그런 이유로 멤버변수를 class쪽에 안 씀
#    overloading이 안 되니 생성자가 하나만 가능 <- 이걸 이용해서 멤버변수를 생성자에서 만드는 경향이 있음
class product:
    # 이 곳에 멤버변수 쓰는 건 의미 없음
    def __init__(self, name, price): # 멤버변수를 만들 때, 하나밖에 만들 수 없는, 생성자를 이용해서 만드는 경향이 있음
        self.name = name
        self.price = price
        # but, 이렇게 해도 외부에서 아무렇게나 멤버변수를 추가할 수 있는 건 마찬가지임...
    def printInfo(self):
        print(self.name, self.price)