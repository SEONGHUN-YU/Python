# -*- coding:utf-8 -*-

import pandas as pd

# pandas의 기본 마인드 : 원본을 건들지 않게 <- 원본에 뭘 수정할면 작업을 해서 다시 대입해야 함

a = pd.DataFrame()
a['이름'] = ['아메리카노', '라떼']
a['가격'] = [5000, 6000]
print(a)
print('-----')

# pd.Series(list 같은 거)
b = pd.Series(['녹차라떼', 7000], index=['이름', '가격']) # 0, 1, ... (list 같은 거라서)
a = a.append(b, ignore_index=True)
                # 기존에 b에서 쓰던 0, 1, ... index 체계를 무시하도록
print(a)
print('-----')

# dict 추가
c = {'이름' : '딸기라떼', '가격' : 8000}
a = a.append(c, ignore_index=True)
    # 애초에 c는 0, 1, ... 체계가 아님
    # dict/pd.DataFrame 체계가 비슷한 듯
print(a)
