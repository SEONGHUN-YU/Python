# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from bs4 import BeautifulSoup

s = "   aaa   "
s = s.strip()

s = "!!!aaa!!!"
s = s.strip("!!!")

huc = HTTPSConnection("movie.naver.com")
huc.request("GET", "/movie/point/af/list.naver")
bs = BeautifulSoup(huc.getresponse().read(), "html.parser", from_encoding="utf-8")
movies = bs.select("td.title")
for m in movies:
    s = m.text.split("\n")
    review = ""
    for w in s[5 : len(s) - 2]: # len - 1과 len - 2까지는 불 필요한 내용, 나머지는 내용칸, \t으로 채워져 있음
        review += w
    review = review.strip("\t")
    print(m.select("a")[0].text) # 제목
    print(m.select_one("em").text) # 점수
    print(review) # 리뷰
huc.close()