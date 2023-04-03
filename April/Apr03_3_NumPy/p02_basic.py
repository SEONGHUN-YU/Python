# -*- coding:utf-8 -*-

# anaconda 설치 -> jupyter notebook으로 작업
#    Python가상환경을 만들어 줌 -> 분석관련 lib들 자동설치해줌
#    jupyter notebook : 브라우저에서 실행하는 웹 베이스
#    한 줄 써서 결과 확인해보고 -> 또 한 줄 써서 결과 확인해보고... => 대화형

#    굳이 가상환경이 필요한가?
#    lib 자동설치 되는 것도 싫고
#    우리 목표는 단순 분석이 아니고 -> 분석결과를 다른데서 쓸 수 있게
#                                        온전한 프로그램 형태를 원함

# 설치 pip install numpy
#    패키지 없고
#    numpy.py
import numpy as np # 이렇게들 많이 하더군요

# 객체지향언어에서 굳이 2차원 list를 하고 있나
#    => 객체 list로 하지 => 그러게요
score = [[100, 90, 80], [50, 30, 100]]
print(type(score))
print(score)
print(score[0])
print(score[0][1])
score[0][1] = 0
# score[1][0:3] = 0 <- 이 방식 불가능 
print(score[1][0:3]) # <- (범위에 접근하는 거)는 가능 
print(score)
print(len(score))

print("----------")

score2 = np.array(score)
print(type(score2))
print(score2) # 가독성이 좋은 듯
print(score2[0])
print(score2[0][1]) # 기존 Python list 스타일
print(score2[0, 1]) # numpy 스타일
score2[0, 1] = 99
score2[1, 0:3] = 0 # slicing : 범위에 값 한꺼번에 넣기
                                # 기존 list는 불가능
print(score2)
print(score2.shape) # 몇행몇열
print(score2.dtype) # 자료형
print(score2.size) # 총 몇개 <- len() 상위호환?


# numpy : 기능 많은 list
#    pandas, matplotlib, tensorflow, ... 후속 기술들이 numpy를 활용함