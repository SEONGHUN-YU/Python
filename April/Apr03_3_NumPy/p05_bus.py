# -*- coding:utf-8 -*-

import numpy as np
from idlelib.iomenu import encoding

# 내린 게 더 많은 정류장 이름
f = open("D:/yu/BusResult.txt", "r", encoding="utf-8")
# f.readlines()의 위험성 - 다 읽어서 \n로 나눠서 list로
#        다 읽어서 RAM에다 넣겠다는 건데
#        전처리를 해오니 가능한 것

# 쌤의 풀이
# stationName, ride, alight = [], [], []
# even = True
# for line in f.readlines():
#     line = line.replace("\n", "").split("\t")
#     if even:
#         stationName.append(line[0][0:len(line[0]) - 2]) # !!
#         alight.append(int(line[1]))
#     else:
#         ride.append(int(line[1]))
#     even = not even

bus_stop_list, on_list, off_list = [], [], []
for line in f.readlines():
    s = line.replace("\n", "").split("\t")
    if "_내" in line:
        bus_stop_list.append(s[0].replace("_내", ""))
        on_list.append(int(s[1]))
    else:
        off_list.append(int(s[1]))
    
bus_stop = np.array(bus_stop_list)
on = np.array(on_list)
off = np.array(off_list)
print(bus_stop[on < off])
busResult = bus_stop[on < off]
for r in busResult:
    print(r)

f.close()