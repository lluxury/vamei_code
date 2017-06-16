import threading
# from multiprocessing.dummy import Process as thr
import time

count = 1
lock = threading.Lock()


class KissThread(threading.Thread):
    def run(self):
        global lock
        lock.acquire()
        global count
        print("Thread # %s:  Pretending to do stuff" % count)
        count += 1
        time.sleep(2)
        print("done with stuff")
        lock.release()

for t in range(5):
    KissThread().start()


#global 的写法怪怪的, 有没有其他写法
#  是一样的,不过赋值一般会放在函数下面,主程序上面,只能在函数中申明,放外面会报错

# 没有.join, 作用及影响?
# 引用了现有类,写了一个方法,
# 没有设置锁,有插队的现象,如何改进

# Thread # 1: Pretending to do stuff
#  Thread # 1: Pretending to do stuff
# Thread # 3: Pretending to do stuff

# 增加锁,现象解决


import threading


class test(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        try:
            print "code one"
        except:
            pass

for i in range(10):
    cur = test()
    cur.start()

for i in range(10):
    cur.join()

# 感觉标准一些,test是类,类运行,写范围,阻塞
# 创建线程,启动线程
