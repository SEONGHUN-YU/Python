# -*- coding:utf-8 -*-

# range : 범위
a = range(3) # 0 ~ 2 (3 - 1)까지
b = range(2, 5) # 2 ~ 4 (5 - 1)까지
c = range(2, 15, 3) # 2 ~ 14 (15 - 1)까지 3칸씩
print(list(a)); print(list(b)); print(list(c))

# 범위표현
# 1 ~ 10까지 들어있는 list
d = range(1, 11); print(list(d))
print("-----")

# tuple : list랑 별 차이가 없어보이는데 <- Python의 꽃?
# 데이터 표현용 컬렉션
# Python의 특징적인 문법에 활용
e = (45, 12, 14, 77)
print(e, type(e), e[0], len(e))

# x = 10; y = 20; z = 30
(x, y, z) = (10, 20, 30) # 변수 여러개 한꺼번에 초기화시킬 때도 쓸 수 있고, ()를 떼도 tuple이 된다
print(x, y, z)
(x, y, z) = (y, z, x) # 변수 여러개 값 바꿔줄 때도 쓸 수 있다
print(x, y, z)