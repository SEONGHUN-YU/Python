# -*- coding:utf-8 -*-
from _datetime import datetime

# [], List, Set, Map
#    list, set, dict, range, tuple, numpy, pandas???
#    numpy, pandas : 정체가 컬렉션

f = open("D:/yu/student0324.csv", "r", encoding="utf-8")

class student:
    
    def __init__(self, s):
        l = s.split(",")
        self.n = l[0]
        self.b = datetime.strptime(l[1], "%Y%m%d")
        self.k = int(l[2])
        self.e = int(l[3])
        self.m = int(l[4])
        
    def printInfo(self):
        print("이름 : %s" % self.n) # getattr
        print("생일 : %s" % self.b)
        print("나이 : %s" % (datetime.today().year - self.b.year + 1)) # age
        print("국어 : %d" % self.k)
        print("영어 : %d" % self.e)
        print("수학 : %d" % self.m)
        print("평균 : %.1f" % float((self.k + self.e + self.m) / 3))
        print("-----")
        
# 객체쪽으로 분석하면 더 편한데...
# numpy, pandas -> 객체 X

students = []
for line in f.readlines():
    s = student(line.replace("\n", ""))
    students.append(s) # 객체 배열 정렬
f.close()

# 객체 배열 정렬
# list에 학생 객체들이 들어있는 상태
# lambda함수 : 이름없는 1회용함수, 객체 정렬할 때는 람다를 써야함
# (lambda p1, p2, ... : return 할 거[return은 생략])(v1, v2, ...)
# ↓ list에 있는 학생객체 하나하나를 s에 넣어서 이름 기준으로 해본 예시
# students.sort(key=lambda s:s.name, reverse=True)
students.sort(key=lambda s:s.k+s.e+s.m, reverse=True) # 성적평균순 정렬

students[0].printInfo() # 최고 성적 학생
print("-----")    
students[-1].printInfo() # 꼴찌 학생