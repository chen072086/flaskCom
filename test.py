#@project:checkDomain
#@author:chenliangfu
#@file:myfile.py
#@time:2018-7-6  15:00:00
#@Description:XX

from functools import wraps
#装饰器   传入的都是函数，返回的还是函数
def my_log(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('hello word')
        func(*args,**kwargs)
    return wrapper

@my_log
def run():
    print('run')

print(run.__name__)

@my_log
def add(a,b):
    c = a+b
    print('该结果集合是%s' %c)

add(3,5)
run()
