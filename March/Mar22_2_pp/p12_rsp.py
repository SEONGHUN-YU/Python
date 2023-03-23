# -*- coding:utf-8 -*-
from random import randint

handTable = [None, "가위", "바위", "보"]
def printRule():
    for i, j in enumerate(handTable):
        if i != 0: # A's Knowledge (condition에 j만 넣음)
            print("%d) %s " % (i, j))

def printPick(user, com):
    print("-----")
    print("나 : %s" % handTable[user])
    print("컴 : %s" % handTable[com])
    
def userPick():
    print("-----")
    userpick = int(input("선택 : "))
    if userpick < 1 or userpick > 3:
        return userPick()
    return userpick
    
def comPick():
    return randint(1, 3)

def judge(user, com):
    if user - com == 0:
        print("무승부"); return False
    elif user - com == -1 or user - com == 2:
        print("패배"); return False
    else:
        print("승리"); return True

def result(count):
    print("%d번 만에 승리" % count)
# for-each는 기능상 부족
# for는 너무 길고 복잡
# -> 쓰지말자 (Java에서의 결론)

printRule()
count = 1 # 전역변수 : 밖에 나와있어서, 아무 스코프에서나 다 쓸 수 있는 변수
while True:
    user, com = userPick(), comPick()
    printPick(user, com)
    if not judge(user, com):
        count += 1
    else:
        break
result(count)

# 어쨌든 한 줄 실행되기 전에 변수가 만들어져 있기만 하면 됨 <- 이건 다시 개념 정리를 해볼 필요가 있을 듯