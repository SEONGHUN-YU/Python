# -*- coding:utf-8 -*-

import numpy as np

a = np.random.randint(1, 10, [3, 5])
print(a)

a[0][1] = 888
a[0, 1] = 999
#            조건, 바꿀값, 대상
b = np.where(a % 2 == 0, 777, a)
print(b)