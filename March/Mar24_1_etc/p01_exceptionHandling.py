# -*- coding:utf-8 -*-

if __name__ == '__main__': # 해도 좋고, 안 해도 상관 없고
    pass

# error : 문법에 안 맞아서 기계어로 번역 안 되는 상황
# warning : 지저분한 소스(프로그램 실행에는 문제없지만, 정리해주는 게 좋음)가 있는 상황
# exception : 프로그램은 완성 되어 있는데, 실행 때, 예외적인 상황 때문에 정상적으로 안 되는 상황

# compiler방식 : .java -컴파일-> .class -실행->
# interpreter방식 : .py -실행->

# Python은 error와 exception의 구분이 모호함

# Java는 exception처리 안 하면 error로 간주했음
# Python은 exception처리 안 하고 싶으면 안 하는 거

try:
    x = int(input("x : ")); y = int(input("y : ")); print(x / y)
    l = [12, 34]; print(l[y])
except Exception as e: # 퉁쳐서 잡아주는 애
    print(e)
    '''except ZeroDivisionError:
        print("나누기 0")
    except IndexError:
        print("리스트에 없는 인덱스")'''
else: # 아무문제 없으면 실행 됨
    print("문제 없음")
finally:
    print("문제가 있든 없든, return보다 먼저 실행됨")
