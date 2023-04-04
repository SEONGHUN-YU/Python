# -*- coding:utf-8 -*-

import numpy as np

# 객체지향언어에서 굳이 다차원 list를... => numpy를 왜...
#    => 후속기술들이 numpy를 쓰니
#    => 남들 다 하는데 못하면 안 되니

# 알고리즘 잘 도는지 테스트 => 더미데이터 만들 때
# 인공신경망 만들 때 => 초기값 넣을 때
# => 어떤 값이 여러개 자동으로 생기기를

# 대부분 float형으로 많이 해주는데
a = np.zeros([3, 5]) # 0으로 꽉 채움
print(a)
print(a.dtype)

# 다른 자료형을 꼭 써야겠다 싶으면
b = np.zeros([2, 3], dtype=np.int64)
print(b)
print(b.dtype)

c = np.ones([3, 4]) # 1로 꽉 채움
print(c)

d = np.empty([2, 5]) # 별 의미없는 값으로 꽉 채움
print(d)

e = np.arange(5) # 0 ~ (5 - 1)까지
print(e)

f = np.arange(2, 7) # 2 ~ (7 - 1)까지
print(f)

g = np.arange(2, 10, 3) # 2 ~ (10 - 1)까지 3칸씩
print(g)

h = np.random.rand(3, 2) # 랜덤(0.0 ~ 1.0), 3x2로
print(h)

i = np.random.randn(3, 2) # 랜덤(평균0이고 표준편차1), 3x2로 
print(i)

j = np.random.randint(2, 10, [3, 2]) # 랜덤(2 ~ (10-1)), 3x2로
print(j)