# -*- coding:utf-8 -*-

class lion():
    def __init__(self, name):
        self.name = name
    
    def printInfo(self):
        print(self.name)

class tiger():
    pass

class elephant():
    pass

# 이 if문의 정체는, 여기서 실행했을 때, 라는 의미
# import당했을 때 말고
if __name__ == "__main__":
    from animal.pet import dog
    d = dog()
    print(id(d))