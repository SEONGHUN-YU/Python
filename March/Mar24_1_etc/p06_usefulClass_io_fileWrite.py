# -*- coding:utf-8 -*-

# f = open("경로", "모드", encoding="utf-8")
f = open("D:/yu/test.txt", "a", encoding="utf-8")
# r : 읽기 모드
# w : 기존에 거 지우고 쓰기
# a(append) : 기존에 거 뒤에 붙여서 쓰기

f.write(input("뭐 : ") + "\n") # Python에서는 \n이 \r\n 느낌인 듯? <- 나중에 찾아봐야할 듯
f.close()

# Python : 그냥 다 따로, 문법이 다 다름
# print(), input()

# Java : 통합된 입출력시스템
#       어떤 장치든 똑같이 작업할 수 있기를 바랬음
#       InputStream/OutputStream
#       ...
#       Buffered가 어쩌고 => 소스가 길다