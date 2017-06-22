#! -*- coding:utf-8 -*-
import gevent
from gevent import monkey;monkey.patch_all()
import urllib2

def get_body(i):
    print "start",i
    urllib2.urlopen("http://cn.bing.com")
    print "end",i

tasks=[gevent.spawn(get_body,i) for i in range(3)]
gevent.joinall(tasks)





import threading
import urllib2

def get_body(i):
    print "start",i
    urllib2.urlopen("http://cn.bing.com")
    print "end",i

for i in range(3):
    t=threading.Thread(target=get_body, args=(i, ))
    t.start()

#代码对比,会乱序?

# monkey可以使一些阻塞的模块变得不阻塞，机制：遇到IO操作则自动切换，手动切换可以用gevent.sleep(0)（将爬虫代码换成这个，效果一样可以达到切换上下文）
# gevent.spawn 启动协程，参数为函数名称，参数名称
# gevent.joinall 停止协程