import re

number = re.compile(r'\d+')

class company:
    companyCount = 0

    def __init__(self,name,age,price):
        self.name = name
        self.age = age
        self.prisssssss = price

    def companyPlayGame(self):
        print(f'实例name：{self.name}')
        print(f'实例age：{self.age}')
        print(f'实例price：{self.prisssssss}')

    def companyWatchTv(self):
        print(f'实例对象WatchTv age：{self.age}')
        print(f'实例对象WatchTv price：{self.prisssssss}')

def test():
    result = re.findall(number,'as3dasd1asd12ads')
    print(result)
    arr = []
    arr.append(1)
    arr.append(2)
    arr.append(3)
    arr.append('apple')
    print(arr)
    if len(arr) == 3 : print("len为3")
    for item in arr:
        print(item)
    if len(arr) == 3:
        return 1
    elif len(arr) == 4:
        return 2
    elif len(arr) == 5:
        return 3
    return result


if __name__ == '__main__':
    abc = test()
    print(f'return result:{abc}')
    c1 = company('sora33',29,999)
    c2 = company('hina',7,299)
    c1.companyWatchTv()
    c2.companyPlayGame()