# -*- coding:utf-8 -*-
from time import sleep

print("ㅋㅋㅋ")         # System.out.println();
print("ㅎㅎㅎ", end="") # System.out.print();
print("%.1f" % 1.23123) # System.out.printf(); Python에서는 쉼표(,)가 아니라 %를 쓴다 
print("%s%03d%.2f" % ('hello', 2, 1.23) )  # printf로 여러개 쓸 때는 % ( , ...)

sleep(5) # 초단위

# Java : compiler방식
#    .java -컴파일-> .class -압축-> .jar
#    .java -> 사용자 컴에 이클립스 설치할 건지? Runnable jar file로 해야지
# Python : interpreter방식
#    .py -실행->