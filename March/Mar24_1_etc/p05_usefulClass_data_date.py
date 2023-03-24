# -*- coding:utf-8 -*-
from datetime import datetime
from time import strftime

# 패키지 없고, from : datetime.py라는 모듈, import : class datetime

now = datetime.today() # class에 들어있는 static 메소드
print(now); print(now.year); print(now.month);

yesterday = datetime(2023, 3, 23); # 특정시간 날짜, 그냥 생성자 쓰면 끝
print(yesterday)
print("-----")

# 패턴 확인
# time.py에 있는 strftime
# help(strftime) <- 여기서

# 데이터 구해오면 거진 str인데
# str -> datetime (parse)
str_date = input("날짜 : ");
when = datetime.strptime(str_date, "%Y%m%d"); print(when)

# datetime -> str (format)
date_str = datetime.strftime(when, "%A"); print(date_str)



# Java : 오래됐음
# Java의 Date객체 : Java초창기에 만들어짐 -> 오래됐음
#       그 시절에는 2000년대에 관심 없었는데
#       옛날에 만들어진 그 Date를 써야하니...

# Python : 나온지 얼마 안 됨
#   2000년대 다 처리되어있음