(flask)[root@iZuf6c03srb2lr8ts2jv6gZ microblog]
#! -*- coding:utf-8 -*-
from multiprocessing import Process as pro
from multiprocessing.dummy import Process as thr

from gevent import monkey; monkey.patch_all()
import gevent


def run(i):
    lists = range(i)
    list(set(lists))

if __name__ == "__main__":

        '''
        多进程
        '''
    for i in range(30):
        t=pro(target=run, args=(5000000,))
        t.start()

        '''
        多线程
        '''
    # for i in range(30):
    #     t=thr(target=run,args=(5000000,))
    #     t.start()

        '''
        协程
        '''
    # jobs = [gevent.spawn(run,5000000) for i in range(30)]
    # gevent.joinall(jobs)
    # for i in jobs:
    #     i.join()

        '''
        单线程
        '''
    # for i in range(30):
    #     run(5000000)


# time python test.py
# ,有什么用?
# 多线程及进程,协程,的故障不是很好排,错位不报错,有没有列子进程故障的方法
# pdb c可以查出来,但是退不出去
# PyCharm 

# 并发10次：【多进程】2.1s 【多线程】3.8s 【协程】4.0s 【单线程】3.5s
# 并发20次：【多进程】3.8s 【多线程】7.6s 【协程】7.7s 【单线程】7.6s
# 并发30次：【多进程】5.9s 【多线程】11.4s 【协程】11.5s 【单线程】11.3s

# 可以看到，在CPU密集型的测试下，多进程效果明显比其他的好，多线程、协程与单线程效果差不多。
# 结论,单台爬虫多线程,单台计算多进程,无要求单线程


