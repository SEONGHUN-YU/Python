# -*- coding:utf-8 -*-

# Java 형변환 : (자료형) 값
# Python에서는 -> 생성자(값)

# input("x : ") # str, 따라서 str + str이 되어버린다

x = int(input("x : "))
y = int(input("y : ")) 
print("-----")
a = x + y; b = x - y; c = x * y; d = x / y; e = x % y
print(a, b, c, d, e)

# Java : ? + String => 붙여서 String으로
# k = 1 + "hi" <- 불가능

# Java : ? * String => 불가능
print(3 * "zs") # *는 repeat처럼 사용됨 (str * int)

# Java : 자료형을 직접 컨트롤 해주는 언어
# Python : 자료형 적절한 걸로 알아서 바꿔줌
print(type(10/4)) # float
print(type(10//4)) # int (//로 나누면 소수점 안 나옴)

x += 3; print(x); y -= 1; print(y)
# Java : 저급 -> 사람이 직접 컨트롤
#             -> 효율적인 프로그램, But 개발이 힘듬 
#        => 컴퓨터쪽에 친화적
# Python : 고급 -> 자동으로 컨트롤 해줌
#               -> 효율성은 떨어짐, But 개발은 쉬움(개발속도, 코드의 길이, ... 이점을 가짐)
#        => 사람쪽에 친화적
#        => 대체할 것이 있으면 없앴음 (i++, j-- 같은 게 없음)
#        => 공부할 거리가 줄어듬