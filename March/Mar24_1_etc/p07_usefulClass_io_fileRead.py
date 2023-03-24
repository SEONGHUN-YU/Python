# -*- coding:utf-8 -*-

f = open("D:/yu/test.txt", "r", encoding="utf-8")
# print(f.read()) # 전체를 다 읽어서, str 한 줄로 만들어줌
# print(f.readline()) # 한 줄씩 읽어서, str로 만들어줌
# print(f.readlines()) # 전체를 읽어서, \n 기준으로 split해서 list로 만들어줌, 웃긴건 \n은 살려놨음

for line in f.readlines(): # 이런식으로 자주 쓸 듯
    print(line.replace("\n", "")) # \n을 없애려면 이렇게 해야하니, 사실상 이런 형태가 고정일듯

f.close()