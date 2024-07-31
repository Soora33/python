
from diffusers import DiffusionPipeline

def test_part1():
    list1 = [1,3,5,7,9]
    list2 = list(map(lambda x: x**2,list1))
    list3 = list(filter(lambda x: x % 3 == 0,list2))
    for item in list3:
        print(item)

def test_part2():
    while True:
        try:
            int(input('input number\n'))
            break
        except ValueError:
            print('error number!')

def test_part3():

    pipeline = DiffusionPipeline.from_pretrained("shibal1/anything-v4.5-clone")
if __name__ == '__main__':
    print("/n")
    test_part3()