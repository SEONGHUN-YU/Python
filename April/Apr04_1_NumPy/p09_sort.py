# -*- coding:utf-8 -*-

import numpy as np

a = np.random.randint(1, 100, 10)
print(a)
print(a[1])
print(a[1:5]) # 1 ~ (5 - 1)까지
print(a[1:7:2]) # 1 ~ (7 - 1)까지, 2칸씩
print(a[:7:2]) # 0 ~ (7 - 1)까지, 2칸씩
print(a[1::2]) # 1 ~ 끝까지, 2칸씩
print(a[::2]) # 0 ~ 끝까지, 2칸씩
print(a[::-1]) # 0 ~ 끝까지, 역순으로
print("-----")

b = np.sort(a) # 오름차순
print(b)
# 내림차순이 따로 없음(오름차순으로 하고, 반대로 빼면 되니까?)
c = np.sort(a)[::-1] # 이런 느낌으로 내림차순을 씀
print(c)
print("-----")

d = np.random.randint(1, 100, [3, 5])
print(d)
e = np.sort(d) # 행방향 정렬, 하나의 row내에서만 정렬시켜줌
print(e)
# e = np.sort(d, axis=1) # <- 행방향 정렬, 이거랑 위에 꺼랑 같음
# print(e)
f = np.sort(d, axis=0) # 열방향 정렬, 하나의 column내에서만 정렬시켜줌
print(f)

# 2차원 : z = [[10, 2],
#              [3, 4]]
#    z[0] = [10, 2]
#    z[0][1] = 2

#    열방향 오름차순
#    z = [[3, 2],
#         [10, 4]]
#    뒤에서부터 접근하니(z[1] -> z[0]) <- 이런 식으로 가니까
#    [[10, 4],
#     [3, 2]]

# 2차원은 내림차순이 제대로 정렬이 안 됨;
i = np.sort(d, axis=0)[::-1] # 열방향, 역순으로 빼기(내림차순) <- 얘는 정렬이 됨
print(i)
#    z = [[10, 2],
#         [3, 4]]
#    행방향 오름차순 정렬시키면
#    z = [[2, 10],
#         [3, 4]]
#    역순 접근하면
#    z = [[3, 4],
#         [2, 10]]
j = np.sort(d, axis=1)[::-1] # 행방향, 역순으로 빼기(내림차순) <- 이건 정렬이 안 됨
# [:, ::-1] 이거쓰면 정렬이 됨 A's Knowledge
print(j)
print("-----")

# 행방향 내림차순은 직접 구현해야 함
kk = []
for dd in d:
    kk.append(np.sort(dd)[::-1])
kk = np.array(kk)
print(kk)