# -*- coding:utf-8 -*-
from http.client import HTTPSConnection

try:
    # HTTP인지 HTTPS인지 체크, HTTPConnection(), HTTPSConnection()
    huc = HTTPSConnection("www.kma.go.kr") 
    # 주소+[포트]까지만 즉, 첫 슬래쉬 전까지만
    huc.request("GET", "/wid/queryDFSRSS.jsp?zone=1168064000") # 요청방식, 나머지 주소
    # 폴더/파일/파라메터 전부 다 즉, 남은 주소 싹 다(첫 슬래쉬 포함)
    hr = huc.getresponse() # 응답내용
    hrBody = hr.read() # 내용 꺼내기
    # print(hrBody)
    print(hrBody.decode()) # 응답내용 한글처리해서 제대로 보려면
except Exception as e:
    print(e)
huc.close()