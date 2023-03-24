# -*- coding:utf-8 -*-

# Python : 예외처리하든지 말든지
#        개발자 됐으면 현업에선 해야지


# Java
#    1) try-catch-finally로 직접 처리
#    2) throw로 미루기 <- 아래와 같은 이유로, Python에는 없음

# Java : 컴파일해서 .jar를 주고 받음 -> 수정이 불가능
# Python : .py를 주고 받음 -> 수정이 가능

class calculator():
    def divide(self, x , y):
        try:
            return x / y
        except Exception:
            print("나누기 0")
        else:
            print("계산 끝")
        finally:
            print("정상이든 비정상이든 어쨌든 끝")