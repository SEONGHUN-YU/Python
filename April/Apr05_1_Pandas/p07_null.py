# -*- coding:utf-8 -*-

import pandas as pd

a = pd.read_csv('D:/yu/titanic.csv')
print(a)

print(a['Age'].isnull()) # 값이 없는지 bool로 return
print(a[a['Age'].isnull()]['Name']) # 나이 정보가 없는 사람이름
                                    # bool이니 masking 활용 가능
                                    
# 값이 없는 거 채우기 <- 뭘로 채울지는 차차 고민해보고
a['Age'] = a['Age'].fillna(0)
print(a['Age'])

# 값이 있는 거 없애기
# pandas가 없다를 표현을 못해서, numpy로 해야 함
import numpy as np
a['Age'] = a['Age'].replace(0, np.nan)
print(a['Age'])