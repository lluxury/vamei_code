#!/usr/bin/env python
#from processing import Process, Queue
from multiprocessing import Process, Queue
import time


def f(q):
    x = q.get()
    print("Process number %s, sleeps for %s seconds" % (x, x))
    time.sleep(x)
    print("Process number %s finished" % x)

q = Queue()
for i in range(10):
    q.put(i)
    i = Process(target=f, args=[q])
    i.start()


print("main process joins on queue")
i.join()
print("Main Program finished")

# 感觉怪怪的,没有锁,结果随机
# 应该是共享一个STDOUT,输出结果乱了,待确认?
