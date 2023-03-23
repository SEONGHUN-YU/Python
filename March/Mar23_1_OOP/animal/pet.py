# -*- coding:utf-8 -*-

# import라는 건
#    Java의 import처럼 : 옵션으로(하든말든)
#    Python의 import처럼 : 사용하려면 필수[import한 파일에 들어있는 소스가 여기에 포함되는 느낌]

from animal.wild import lion # 안전하게 import하려면 if문처리 해줄 것

class dog():
    pass

class cat():
    pass

# Python : interpreter
#        따로 main()이 없음 -> 엄격하지 않음
#        => 그냥 여기다 쓰지 뭐? <- 이런게 가능
l = lion("심바")
l.printInfo()