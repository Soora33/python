
import re

def test_part1():
    pattern = re.compile(r'你真的好(.*)帅')
    text = '你真的好nm"handsome"1+1=2帅'
    result = re.findall(pattern,text)
    print(result[0])



if __name__ == '__main__':
    print("/n")
    test_part1()