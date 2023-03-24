# -*- coding:utf-8 -*-

# 역별 이용객수(타고+내리고) top10

f = open("D:/yu/subway.csv", "r", encoding="utf-8")

class subwayCount:
    def __init__(self, name, on_off):
        self.name = name
        self.on_off = on_off
    
swdict = {}
for line in f.readlines():
    line = line.replace("\n", "").split(",")
    if line[4] in swdict:
        swdict[line[4]] = line[5]+line[6]
    else:
        swdict[line[4]] = line[5]+line[6]
f.close()

swlist = []
for k, v in swdict.items():
    swlist.append(subwayCount(k, v))
swlist.sort(key=lambda obj:obj.on_off, reverse=True)
for index, obj in enumerate(swlist):
    if index == 10:
        break
    print(obj.name, obj.on_off)