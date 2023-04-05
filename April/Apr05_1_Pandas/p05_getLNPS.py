# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from studykey import studykey
from json import loads

# M_NAME : 시장이름
# A_NAME : 품목
# A_PRICE : 가격
# M_TYPE_NAME : 시장종류
# M_GU_NAME : 구

def parsing(a, b, c, d, e):
    a = a.replace(',', '.')
    b = b.replace(',', '.')
    c = c.replace(',', '.')
    d = d.replace(',', '.')
    e = e.replace(',', '.')
    return '%s,%s,%s,%s,%s\n' % (a, b, c, d, e)

huc = HTTPConnection('openapi.seoul.go.kr:8088')
f = open('D:/yu/LNPS.csv', 'a', encoding='utf-8')
for start in range(1, 450001, 1000):
    length = '%d/%d' % (start, (start + 999))
    huc.request('GET', '/' + studykey().Seoul() + '/json/ListNecessariesPricesService/' + length)
    for r in loads(huc.getresponse().read())['ListNecessariesPricesService']['row']:
        f.write(parsing(r['M_NAME'], r['A_NAME'], r['A_PRICE'], r['M_TYPE_NAME'], r['M_GU_NAME']))
    print(length)
f.close()
huc.close()
