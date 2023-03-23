# -*- coding:utf-8 -*-

# Java : perfect한 객체지향언어
#    => 무조건 OOP를 해라, 이런 구조
#    => 1file == 1class
#    => 다른 개발자들이 봤을 때 class라는 걸 바로 인지할 수 있게끔 첫 글자를 꼭 대문자로 하는 문화가 있음
#    => 접근제어자 있음 => 데이터 안전하게
#    OOP의 좋은 점
#        코드 재활용
#        -> Dog.java -> .jar로 만들어서 또 쓰자

# Python : hybrid한 객체지향언어
#    => 하기 싫으면 안 해도 됨
#    => class만들 때 파일을 따로 만들던지 말던지 맘대로 해라!
#    => 첫 글자를 대문자로 하던지 말던지!
#    접근제어자 없음 => 외부에서 데이터를 안전하게 건들던지 말던지 => 캡슐화 X => 패턴 프로그래밍 X

#    Java 하다가 온 사람들은 첫 글자를 대문자로 쓸 것 ㅋ
class dog:
    name = None # 의미없음
    age = None # 앞으로는 안 쓸 것
    
    # 메소드는 첫번째 parameter로 self를 쓰게 되어있음, 두번째부터는 맘대로
    def bark(self, count):
        for _ in range(count): # i를 안 쓸거면, _로 지워도 됨
            print("멍", end="")
            
    def printInfo(self):
        print(self.name) # Java의 this.name 같은 것
        print(self.age) # Python은 self. 로 쓰고 생략 불가능함 <- 중요
    
    @staticmethod    
    def test():
    # self를 빼고 만들면 static메소드처럼 됨, 필수는 아니지만 @staticmethod를 static메소드 위에 달아주는 게 좋음 
        print("이거는 static메소드")
        
d = dog() # Java의 경우 : Dog d = new Dog();
d.name = "후추"; d.age = 3; print(d.name); print(d.age)
d.weight = 5; print(d.weight) # <- 이런식으로 멋대로 추가할 수가 있어서 class쪽에 만들어도 의미가 없음
dog.bark(d, 5) # 클래스명.메소드명(객체, ...) <- 메소드 호출 (오리지널 문법)
# d.bark(5) # 이 방식으로 메소드 호출할 때는 self는 빼야 함 (신형 문법)
print("-----")
d.printInfo()
print("-----")
dog.printInfo(d)

# static멤버변수 : 메모리 아끼기 위해 씀 <- 메모리 신경 안 쓰는 Python에는 없음
# static메소드 : 메모리 아끼기 위해 씀 <- 얘는 객체 안 만들어도 쓸 수 있다는 점 때문에 Python에도 있음
dog.test() # <- 객체(인스턴스) 생성 없이도 사용 가능