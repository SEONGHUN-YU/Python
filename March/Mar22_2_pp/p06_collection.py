# -*- coding:utf-8 -*-

# Java : [], List, Set, Map

# list
a = [123, 234, 5, 567, 678, 321, 65]
str = "뭔가 글자를 좀"
print(str[1]); print(str[1:4]); print(str[-1])

# 부터는 항상 나오고 까지가 항상 짤림
print(a[0])
print(a[0:3]) # index가 [0, 1, 2] 0부터 (3 - 1)까지
print(a[0:5:2]) # index가 [0, 2, 4] 0부터 (5 - 1)까지 2칸씩
print(a[-1]) # 뒤에서 1번째
print(a)

a.append(999) # 맨뒤에 추가
a.insert(1, 0) # 특정위치에 추가
a[0] = 10 # 값 수정
del a[0] # 값 삭제
a.sort() # 오름차순
a.sort(reverse=True) # 내림차순

# 객체 정렬은? <- 다음시간에
print(a)
print("-----")

# set : 중복제거, 순서가 지멋대로임 <- 이렇다보니 잘 안 썼었음
b = {"a", "a", "b", "qwe", "b"}; print(len(b)); print(list(b))

# dict : 순서개념 X, key-value
c = {"키" : 180, "몸무게" : 80}; print(c['키'])

# list + dict = JSON
print(list(c.keys())); print(list(c.values())); print(list(c.items()))

print("시력" in c) # "시력"이라는 key값이 c라는 dict에 존재하는지 bool 리턴
print("키" in c)