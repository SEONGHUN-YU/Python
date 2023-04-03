# -*- coding:utf-8 -*-

import numpy as np
from idlelib.iomenu import encoding
# from collections import defaultdict
# onSum = defaultdict(int)
# offSum = defaultdict(int)

# Python 100% 컨셉 <- 이번엔 이 컨셉으로
# Hadoop으로 전처리 -> Python으로 마무리 <- 다음에 할 컨셉

# subway.csv
# 역이름별로 탄사람수, 내린사람수 합계내서
# 적자보는 역 이름 확인(내린사람수가 더 많은 역)
f = open("D:/yu/subway.csv", "r", encoding="utf-8")

onSum, offSum = {}, {} # ({}, {})
for line in f.readlines():
    line = line.replace("\n", "").split(",")
    if line[4] in onSum:
        onSum[line[4]] += int(line[5])
        offSum[line[4]] += int(line[6])
    else:
        onSum[line[4]] = int(line[5])
        offSum[line[4]] = int(line[6])
    
name_list, on_list, off_list = [], [], [] # ([], [], [])
for k, v in onSum.items():
    name_list.append(k)
    on_list.append(v)
    off_list.append(offSum[k])
    
name = np.array(name_list)
on = np.array(on_list)
off = np.array(off_list)
print(name[on < off])

f.close()