# -*- coding:utf-8 -*-

# Java의 import
# 패키지명.클래스명 변수명 = new 패키지명.클래스명(); <- 너무 길잖아 import 시켜
# com.yu.mar23.product.Product p = new com.yu.mar23.product.Product();
# 너무 길다 -> 패키지명 생략하자 -> import하고 나면
# Product p = new Product(); [클래스명 변수명 = new 클래스명();] 으로 바뀜
# Java의 import는 그저 소스 짧게 쓰고 싶을 때 쓰는 선택사항임, 필수사항X (다만 길어짐)

# Python의 import는 다른 모듈에 있는 거 가져올려면 무조건 써야하는 필수사항

# import animal.wild # import 패키지명.모듈명 ★ 1번째 방법
# l = animal.wild.lion('심바') # 패키지명.모듈명.클래스명(...)
# l.printInfo()

# import animal.wild as aw # import 패키지명.모듈명 as 별칭 ★ 2번째 방법
# l = aw.lion('심바') # 별칭.클래스명(...)
# l.printInfo()

# 여기서 lion이라고 쓰면 animal.wild에 있는 거다 <- 라고 선언하는 것
from animal.wild import lion # from 패키지명.모듈명 import 가져올 거 ★ 3번째 방법 + as도 가능

# 저렇게 가져왔는데, 이 모듈에 있는 거랑 이름이 겹치면, 이 모듈에 있는 걸로 인식
# def lion(name): # 이런식으로 이름이 겹칠 경우
#     print(name)

l = lion('심바') # 가까운 쪽에 있는 것, 의도치 않게 def가 실행되어버린다던지, 하는 문제가 있음 
l.printInfo()


# animal패키지 > pet모듈 > lion클래스
# 현재 이 모듈은 p06모듈


# Java
#    project
#    package
#    class(.java 파일)
#    Java는 class단위로 작업하고 -> .jar로 만들어서 -> 공유하는 문화가 있음
#    class명 중복이 필연적임 -> package명으로 구분하게 됨
#    중복을 피하기 위해 package필수, package명 중복 안 되게 잘 지어야 함

# Python
#    project <- 이건 억지로 짜냄 (없다고 봐도 무방)
#    package
#    module(.py 파일)
#    class
#    module단위로 작업 -> 공유하는 문화 여기도 있음
#    이름이 중복될텐데 -> 그러든지~ 신경 안 씀 (자유의 언어, 혼란의 언어) -> package가 필수가 아님
#    -> 그러다보니 패키지명을 대충 지음