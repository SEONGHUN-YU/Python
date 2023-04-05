# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from studykey import studykey
from xml.etree.ElementTree import fromstring

# 2016 ~ 2022
# 5.1 ~ 10.31

# 날짜, 물가, 집, 공원
# MOSQUITO_DATE, MOSQUITO_VALUE_WATER, MOSQUITO_VALUE_HOUSE, MOSQUITO_VALUE_PARK

def parsing(a, b, c, d):
    return '%s,%s,%s,%s\n' % (a, b, c, d)

huc = HTTPConnection('openapi.seoul.go.kr:8088')
f = open('D:/yu/mosquito.csv', 'a', encoding='utf-8')
for y in range(2016, 2023):
    for m in range(5, 11):
        for d in range(1, 32):
            length = '%d-%02d-%02d' % (y, m, d)
            huc.request('GET', '/' + studykey().Seoul() + '/xml/MosquitoStatus/1/1/' + length)
            r = fromstring(huc.getresponse().read()).find('row')
            if r != None:
                f.write(parsing(r.find('MOSQUITO_DATE').text, r.find('MOSQUITO_VALUE_WATER').text,
                                r.find('MOSQUITO_VALUE_HOUSE').text, r.find('MOSQUITO_VALUE_PARK').text))
f.close()
huc.close()
# + : 문자열 객체가 있어야 뒤에 붙이는데 소름