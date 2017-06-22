
import time
def war(name):
    def cost(*args, **kwargs):
        start =time.time()
        name(*args,**kwargs)
        stop = time.time()
        print("run time is %s" % (stop - start))
    return cost

@war
def info():
    time.sleep(3)
    print('we are family!')

@war
def auth(name, password):
    time.sleep(2)
    print('login success!')

@war
def ero(x):
    time.sleep(1)
    print('hello %s' % x)

info()
auth('xyz',123)
ero('xyp')

#比较标准的用法,装饰器变量要写成*args才能对应多处使用

import time
def war(name):
        def cost():
            start =time.time()
            name()
            stop = time.time()
            print("run time is %s" %(stop-start))
        return cost
@war
def info():
    time.sleep(3)
    print('we are family!')

info()
#仅仅是用法示例