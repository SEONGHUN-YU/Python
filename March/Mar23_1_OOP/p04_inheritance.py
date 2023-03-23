# -*- coding:utf-8 -*-

# Java의 abstract는 Java에만 있는 거

# Java
#    생성자가 상속 안 됨

# Python
#    생성자가 상속이 안 된다면 매우 곤란할텐데? -> 멤버변수가 상속 안 되겠는데?
#    이렇다보니, Python은 생성자가 상속이 됨
class avengers:
    # Python은 보통 생성자에서 멤버변수를 정의하는 편
    def __init__(self, name, age): 
        self.name = name
        self.age = age

    def show(self):
        print(self.name)
        print(self.age)
        
a = avengers('a', 1)

class human():
    def eat(self):
        print("냠")

# 다중상속 문제 <- 객체지향 언어들의 Hot한 주제
# Java : 다중상속 X
# Python : 다중상속 O
class ironman(avengers, human): # 상속시키려면 클래스 만들 때 ()에 상속받을 클래스를 넣는다
    # overriding : 상속받은 거 기능 바꾸는 중
    # overloading : 메소드명이 같고, 파라메터가 다른 거
    def __init__(self, name, age, ai): # 이걸 오버라이딩이라 불러야할지, 오버로딩이라 불러야할지... 상속받은 거 맞긴 한가?
        avengers.__init__(self, name, age) # <- 이것도 문제없이 실행 됨, 오리지널 스타일임
        self.ai = ai
        # 클래스명.메소드명(객체, a, b, c) <- Python 오리지날 스타일
        
        # super().__init__(name, age)
        # 객체.메소드명(a, b, c) <- Java 스타일
# A's Knowledge : 클래스가 아니라 객체에서 접근할 수 있는 게 super의 장점

    def attack(self):
        print("빔")
        
    def show(self):  # 오버로딩은 없지만, 오버라이딩은 얼마든지 가능
        avengers.show(self) # super().show()
        print(self.ai)

i = ironman("토니", 40)
i.show()
i.eat() # 다중상속 이용해서 호출한 것

# 본명, 나이 속성이 있었는데
# ai 컴퓨터이름 속성을 추가하고 싶음
# 보통, 생성자에서 멤버변수를 결정함
# 생성자가 상속되긴 함
# 상속받은 생성자를 좀 바꾸자 : 생성자 오버라이딩 (이건 Java에 없는 거임)

