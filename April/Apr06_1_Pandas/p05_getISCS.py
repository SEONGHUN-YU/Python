# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from studykey import studykey
from json import loads

# INDUTY_DESC : 업종
# ADRES_CN2 : 주소
# PRDLST_DESC : 품목
# PC : 가격

def parsing(a, b, c, d):
    a = a.replace(',', '.')
    b = b.replace(',', '.')
    c = c.replace(',', '.')
    return '%s,%s,%s,%.0f\n' % (a, b, c, d)

huc = HTTPConnection('openapi.seoul.go.kr:8088')
f = open('D:/yu/ISCS.csv', 'a', encoding='utf-8')
for start in range(1, 4002, 1000):
    length = '%d/%d' % (start, start + 999)
    huc.request('GET', '/' + studykey().Seoul() + '/json/IndividualServiceChargeService/' + length)
    for s in loads(huc.getresponse().read())['IndividualServiceChargeService']['row']:
        f.write(parsing(s['INDUTY_DESC'], s['ADRES_CN2'], s['PRDLST_DESC'], s['PC']))
f.close()
huc.close()