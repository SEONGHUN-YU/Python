# -*- coding:utf-8 -*-
from idlelib.iomenu import encoding

# 이름, 생일(YYYYMMDD), 국어, 영어, 수학

f = open("D:/yu/student0324.csv", "a", encoding="utf-8")
n, b, k, e, m = input("이름 : "), input("생일(YYYYMMDD) : "), input("국어 : "), input("영어 : "), input("수학 : ")
f.write("%s,%s,%s,%s,%s\n" % (n, b, k, e, m))
f.close()