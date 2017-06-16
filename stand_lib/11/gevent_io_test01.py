#! -*- coding:utf-8 -*-
from gevent import monkey
monkey.patch_all()
import gevent
import time
import threading
import urllib2


def urllib2_(url):
    try:
        urllib2.urlopen(url, timeout=10).read()
    except Exception, e:
        print e


def gevent_(urls):
    jobs = [gevent.spawn(urllib2_, url) for url in urls]
    gevent.joinall(jobs, timeout=10)
    for i in jobs:
        i.join()


def thread_(urls):
    a = []
    for url in urls:
        t = threading.Thread(target=urllib2_, args=(url,))
        a.append(t)
    for i in a:
        i.start()
    for i in a:
        i.join()

if __name__ == "__main__":
    urls = ["https://www.bing.com/"]*10
    t1 = time.time()

gevent_(urls)
t2 = time.time()
print 'gevent-time:%s' % str(t2-t1)

thread_(urls)
t4 = time.time()
print 'thread-time:%s' % str(t4-t2)


# pip install gevent
# io密集型
# 300次差0.3秒 感觉测试方法会有点问题, 理论上并发大,协程优势,但不明显
