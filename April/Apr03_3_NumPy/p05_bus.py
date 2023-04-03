# -*- coding:utf-8 -*-

import numpy as np
from idlelib.iomenu import encoding

# 내린 게 더 많은 정류장 이름
f = open("D:/yu/BusResult.txt", "r", encoding="utf-8")
# f.readlines()의 위험성 - 다 읽어서 \n로 나눠서 list로
#        다 읽어서 RAM에다 넣겠다는 건데
#        전처리를 해오니 가능한 것

bus_stop_on, bus_stop_off, on_list, off_list = [], [], [], []
for line in f.readlines():
    s = line.replace("\n", "").split(" ")
#     if "_타" in s:
#         bus_stop_on.append(s[0])
#         on_list.append(s[1])
#     else:
#         bus_stop_off.append(s[0])
#         off_list.append(s[1])
# bs_on = np.array(bus_stop_on)
# bs_off = np.array(bus_stop_off)
# on = np.array(on_list)
# off = np.array(off_list)
# print(bs_on[on < off])
# print(bs_off[on < off])
f.close()