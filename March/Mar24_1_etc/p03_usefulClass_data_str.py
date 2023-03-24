# -*- coding:utf-8 -*-

s = "유용한 클래스 데이터 관련 str"

help(str)
print(s.startswith("유")) # "유"로 시작하는지
print(s.replace("클래스", "class")) # 클래스 -> class
print(len(s)) # 글자 수가 몇 자인지
print(s[1]) # 두번째 글자는?

# Java의 String.format
# print라서 된 게 아니고 Python은 그냥 string이 기본으로 지원해줌...와우
s2 = "시력 : %.2f, 키 : %d" % (1.23, 180); print(s2)

# 문자열 결합
s3 = "ㅋㅋㅋ"; s3 += "ㅎㅎㅎ"; s3 += "ㅇㅇ"
# Java : 이런 식으로하면 메모리상에서 난리가 나니 -> StringBuffer를 써라
# Python : 효율성이 뭔데?
print(s3)

# 문자열 분리
s4 = "ㅋㅋㅋ ㅎㅎㅎ ㅡㅡ ㅠㅠ"; s5 = s4.split(" "); print(s5)
# Java
#   원하는 거 꺼낼 때 .split() => 배열로
#   차례대로 사용 StringTokenizer => while로 상대