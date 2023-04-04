# -*- coding:utf-8 -*-

import pandas as pd, numpy as np

# 쌩 Python list
a = pd.DataFrame()
a["이름"] = ["홍", "김"]
a["나이"] = [30, 40]
print(a)
print("-----")

# np.array(로 뭔가 작업을 해서 넣게 될 것)
b = pd.DataFrame()
b["이름"] = np.array(["홍", "김"])
b["나이"] = np.array([30, 40])
print(b)
print("-----")

# 2차원 쌩list 또는 np.array
c = np.array([["홍", 30], ["김", 40]])
c = pd.DataFrame(c, columns=["이름", "나이"])
print(c)
print("-----")

# 우리가 주로 쓰던 Data구조는 list + dict 였는데
# dict + list
d = {
        "이름" : ["홍", "김"],
        "나이" : [30, 40]
    }
d = pd.DataFrame(d)
print(d)
print("-----")

# list + dict
e = [
        {"이름" : "홍", "나이" : 30},
        {"이름" : "김", "나이" : 40}
    ]
e = pd.DataFrame(e)
print(e)