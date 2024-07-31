import os

import mysql.connector

# 将大于50的加入num2
num1 = [12,40,24,215,57,89,40,46]
# 列表生成器
num2 = [num for num in num1 if num > 50]

print(num2)

# 读取当前目录下
nowDir = [d for d in os.listdir(".")]
print(nowDir)

# 读取
with(open('test.py','r')) as f:
    for ff in f:
        pass
        # print(ff)

# 写入
with(open('a.py','w')) as wf:
    wf.write("test")
    wf.write("where")
    wf.close()

# shutil.copy('day01.py','day00.py')

# 获取当前绝对路径
print(os.path.abspath('.'))
# 拼接路径，会自动转换window和linxu的斜杠
print(os.path.join(os.path.abspath('.'),'mkdir'))
# 获得文件后缀
print(os.path.splitext('/path/to/file.txt')[1])

class Student:
    def __init__(self,name,age,price):
        self.name = name
        self.age = age
        self.price = price

if __name__ == '__main__':
    student = Student('a',12,'a')
    print(student.name)
    print(student.age)
    print(student.price)

conn = mysql.connector.connect(user='root', password='LYproject33', database='sora33')
cursor = conn.cursor()
cursor.execute('select * from sora_user')
result = cursor.fetchall()
for result in result:
    print(result)
conn.close()

