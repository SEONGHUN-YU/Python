# -*- coding:utf-8 -*-

# Python은 다 객체라서 Call by Reference만 있음
d = 10 # d라는 변수 만들고 값 10을 넣음
e = 10

def test(a, b, c):
    print(a, b[0], c[0])
    a = 100
    b[0] = 100
    c = [100, 200]
    d = 100 # d 새로 만든 거임
    global e # 앞으로 나오는 e들은 전부 바깥쪽에서 선언한 e로 취급
    e = 100 # 5번줄의 그 e <- global의 효과
    print(a, b[0], c[0], d, e)
    
a = 10
b = [10, 20]
c = [10, 20]
print(a, b[0], c[0], d, e)
test(a, b, c)
print(a, b[0], c[0], d, e)