# -*- coding:utf-8 -*-
from idlelib.iomenu import encoding

# 비정형데이터 txt 구해서
# 1) 콘솔출력
# 2) wordcount : 무슨 단어가 몇 번 나왔나
# 유비가, 자윽한, 이
# 유비, 조조 중에 어떤 단어가 더 자주 나오는지
# 요즘 트렌드 키워드는 어떤 건지

# 서버급컴퓨터 여러대로 병렬처리 : hadoop으로 전처리
# hadoop으로 전처리 하고나면 용량이 확 줄어듬 -> 그 후에 Python으로 처리

f = open("D:/yu/TKs.txt", "r", encoding="utf-8")

wordCountDict = {}
for line in f.readlines():
    for word in line.replace("\n", "").split(" "):
        if word in wordCountDict: # 등록된 단어임 : 갯수 올리기
            wordCountDict[word] += 1
        else: # 그런 단어 처음 : dict에 추가
            wordCountDict[word] = 1
f.close()

# dict : 순서개념X
# 횟수기준 top10 -> 객체 배열로 정렬 (tuple 배열로도 가능) 
class wordcount:
    def __init__(self, word, count):
        self.word = word
        self.count = count

wordCountlist = []
for k, v in wordCountDict.items():
    wordCountlist.append(wordcount(k, v))
wordCountlist.sort(key=lambda wc:wc.count, reverse=True)
for index, obj in enumerate(wordCountlist):
    if index == 10:
        break
    print(obj.word, obj.count)

"""templist = []
for k, v in wordCountDict.items():
    templist.append((k, v))
templist.sort(key=lambda x :x[1], reverse=True)
for i, s in enumerate(templist):
    print(s)
    if(i==9):
        break"""