# -*- coding:utf-8 -*-

# 모나미153, 500원, 빨간색인 펜
# 정보출력
# 그램123, 1000000원, i7-1234, 램16기가, 하드 500인 컴퓨터
class product():
    def __init__(self, name, price):
        self.name = name; self.price = price
    
    def show(self):    
        print(self.name); print(self.price)
        
class pen(product):
    def __init__(self, name, price, color):
        super().__init__(name, price) # product.__init__(self, name, price)도 같은 효과
        self.color = color
    
    def show(self):
        super().show(); # product.show(self)로도 가능
        print(self.color)
    
class eDevice():
    def __init__(self, eGrade):
        self.eGrade = eGrade
        
    def show(self):    
        print(self.eGrade)

# Java를 포함한 대부분의 언어 : 다중상속 불허
# Python : 다중상속 가능

# 다중상속 시켜봄, 이 때 생성자는 어떻게 되는지?, 상속해준 클래스에도 같은 이름의 메소드가 있으면?
class computer(product, eDevice): # 순서상 product의 것을 오버라이딩함
    def __init__(self, name, price, eGrade, cpu):
        product.__init__(self, name, price)
        eDevice.__init__(self, eGrade)
        self.cpu = cpu
        
    def show(self):
        product.show(self)
        eDevice.show(self)
        print(self.cpu)
    
    # product에도 __init__, show 있음
    # eDevice에도 __init__, show 있음
    # 메소드명이 같은데, 오버라이딩하면 어떤 게 대상이 되는지? -> 맨 왼쪽 꺼로 인식함 이 경우는 product

pen('모나미153', 500, '빨강').show(); print("-----")
computer('그램123', 1000000, 5, 'i7-1234').show()