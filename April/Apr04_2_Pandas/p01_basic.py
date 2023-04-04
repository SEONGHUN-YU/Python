# -*- coding:utf-8 -*-

# NumPy
#    좋은 list
#    객체놔두고?
#        list -> index로 접근 -> 소스 가독성이 안 좋음
#    선수과정
# Pandas(Python Data Analysis Library?) - pd.DataFrame 
#    ↑ 사실 NumPy보다 이게 본체라고 봐야함
#    대부분의 데이터는 2차원
#    엑셀 표

# 설치 pip install pandas

import pandas as pd

# list 같은 거
a = pd.Series([1211, 2312354, 342, 123])
print(a)
print(a[0])
print("-----")

# 엑셀 표 같은 거 <- 주력
# R의 DataFrame에도 똑같은 거 있긴한데 R을 안 써서...
b = pd.DataFrame()
b["이름"] = ["새우깡", "양파링", "맛동산"]
b["가격"] = [3000, 3500, 2500]
print(b)
print("-----")
print(b["이름"]) # 특정필드(column)만 조회
print("-----")
b = b.set_index(b["이름"]) # 앞으로 이름으로 데이터 찾겠다
print(b)                   # PK설정하는 느낌
print("-----")
print(b.loc["새우깡"]) # set_index 설정해줘야만 loc 가능
print("-----")
print(b.iloc[1]) # 1번데이터 찾기