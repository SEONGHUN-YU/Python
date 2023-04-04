# -*- coding:utf-8 -*-

f = open("D:/yu/kma.csv", "r", encoding="utf-8")

wSum, wCnt = {}, {}
for line in f.readlines():
    s = line.replace("\n", "").split(",")
    if (s[2] + '시') in wCnt:
        wSum[s[2] + '시'] += float(s[3])
        wCnt[s[2] + '시'] += 1
    else:
        wSum[s[2] + '시'] = float(s[3])
        wCnt[s[2] + '시'] = 1
        
f.close()
        
hours, temps = [], []
for k, v in wCnt.items():
    hours.append(k) 
    temps.append(wSum[k] / v) # 시간대별 평균기온
    
import numpy as np
h = np.array(hours)
t = np.array(temps)
print(hours[np.argmax(t)], hours[np.argmin(t)])  # 제일 더운 시간대, 제일 추운 시간대
# argmax, argmin은 동점상황일 때 제일 앞에 거 하나만 나옴, 이렇게 짜면 동점처리가 안 되는 문제가 있음
print(temps[np.argmax(t)], temps[np.argmin(t)])  # 최고기온, 최저기온

print(np.min(temps)) # 최저기온
print(h[t == np.min(temps)], t[t == np.min(temps)])

# 평균기온보다 더운 시간대, 기온
print(np.mean(temps)) # 평균기온
print(temps > np.mean(temps))
h2 = h[temps > np.mean(temps)]
t2 = t[temps > np.mean(temps)]

for i in range(h2.size):
    print(h2[i], t2[i])