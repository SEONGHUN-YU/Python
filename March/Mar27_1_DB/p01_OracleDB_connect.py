# -*- coding:utf-8 -*-
from cx_Oracle import connect

# Java
#    JDBC -> ConnectionPool -> MyBatis
#        미리 연결객체 만들어놓고 쓰니, 빠름
#        SQL을 xml에 쓰니 유지보수 편해짐
#        자동으로 객체로 만들어주는

# Python
#    작업이 편한 게 중요하지, 빠른데에 관심이 없음
#    interpreter언어가 유지보수 얘기가 통하나...
#    객체에 별 관심이 없음
#    => JDBC 느낌

try: # 되는지 안 되는지 확인용
    # connect("") 안에 써야할 건 <- sqlplus에서 접속할 때 쓰는 형식
    con = connect("databig/987654321@192.168.0.152:1521/xe")
    # sqlplus 아이디/비번@주소:포트/SID <- Java쪽에서 썼던 양식이랑 다름
    print(con)
except Exception as e:
    print(e)
con.close()

# 아래 작업을 했음에도 어쩔 땐 eclipse에서 자동완성이 안 되기도 함
#    자동완성이 안 되면
#    Window -> Preferences -> PyDev -> Python Interpreters
#    -> Forced Builtins -> New -> cx_Oracle 추가하고 Apply -> eclipse 재부팅

# cx_Oracle.py : instantclient가 필요함 (ojdbc.jar 같은 거)
#    1) instantclient 폴더로 가서 경로 확보
#        C:\Users\sdedu\Desktop\instantclient_21_8
#    저 경로 속에 있는 거 어디서든 쓸 수 있게 해놔야 함 => PATH설정이 필요
#    2) 내 PC 우클릭 -> 속성 -> 고급 시스템 설정 -> 고급 탭 -> 환경 변수
#        지금 로그인한 사용자쪽에만 할 건지 : 사용자 변수(윗쪽)
#        어떤 사용자든지 다 해줄 건지 : 시스템 변수(아랫쪽)
#    3) Path쪽 찾아가서
#        새로 만들기 -> 1)에서 확보해놓은 경로 붙이고 확인연타
#    4) 시작 -> cmd -> sqlplus 쳐서 뭔가 나오면 성공 

# 시작 - cmd
#    pip install 설치할모듈명
#    pip install cx_Oracle <- 위의 작업하기 전에 이거 먼저 ★★★

# Python
#    1) 똑같음
#    2) Python도 개발자들이 작업한 거 공유하는 문화가 있음
#    => Oracle측에서 작업해준 cx_Oracle.py를 쓰면 됨
#    3) 2번이 오죽하면 => pip이 생김

# Java
#    1) DB메이커가 얼마나 다양한데
#    Java측에서 그거 연결하는 드라이버를 어떻게 다 작업을 해주나
#    => 없음 => 직접 만들어서 써야 함
#    2) Java는 개발자들이 자기가 작업한 거 공유하는 문화가 있음
#    => Oracle측에서 작업해준 ojdbc?.jar를 쓰면 됨
#    3) 2번이 오죽하면 => maven(중앙제어시스템)이 생김