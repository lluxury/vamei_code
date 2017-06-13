#!/usr/bin/env_python
#from processing import Process, Queue
from multiprocessing import Process, Queue, Pool
import time, sys
import subprocess
from IPy import IP

q = Queue()
ips = IP("10.0.1.0/24")

def f(i, q):
	while True:
		if q.empty():
			sys.exit()
		print("Process Number: %s " % i )
		ip = q.get()
		ret = subprocess.call("ping -c 1 %s" % ip,
							shell=True,
							stdout=open('/dev/null', 'w'),
							stderr=subprocess.STDOUT)
		if ret == 0:
			print("%s: is avlive" % ip)
		else:
			print("Process Number: %s didi't find a response for %s" % (i, ip))
			pass


for ip in ips:
	q.put(ip)


for i in range(50):
	p = Process(target=f, args=[i,q])
	p.start()

print("main process joins on queue")
p.join()
print("Main Program finished")

#主进程没锁住,输出的中间弹出来了,有机会优化下
#目测运行还正常,ip做队列,跑了50个进程
#p构造语句,p开台,循环50次, q放队列放250个, 只要队列不为空就一直跑