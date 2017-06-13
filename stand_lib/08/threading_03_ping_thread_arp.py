from threading import Thread
import subprocess
import Queue
import re

num_ping_threads = 3
num_arp_threads = 3
in_queue = Queue.Queue()
out_queue = Queue.Queue()

ips = ["223.5.5.5", "223.6.6.6", "114.114.114.114", "8.8.8.8", "7.8.9.10"]

def pinger(i, iq, oq):
    '''PING SUBNET'''
    while True:
        ip = iq.get()
        print("Thread %s: Pinging %s" % (i, ip))
        ret = subprocess.call("ping -c 1 %s" % ip,
                        shell=True,
                        stdout=open('/dev/null', 'w'),
                        stderr=subprocess.STDOUT)
        if ret == 0:
            #print("%s: is alive" % ip)
            #place valid ip address in next queue
            oq.put(ip)
        else:
            print("%s: is not respond" % ip)
        iq.task_done()

def arping(i, oq):
    '''grabs a valid IP address from a queue and gets macaddr'''
    while True:
        ip = oq.get()
        print("Thread %s: Pinging %s" % (i, ip))
        p = subprocess.Popen("arping -I eth1 -c 1 %s" % ip,
                            shell=True,
                            stdout=subprocess.PIPE)
        out = p.stdout.read()

        #match and extract mac address from stdout
        result = out.split()
        # Unicast reply from 192.168.0.151 [64:00:6A:14:3A:D4]  0.710ms
        pattern = re.compile(":")
        macaddr = None
        for item in result:
            if re.search(pattern, item):
                macaddr = item
        print("IP address: %s| Mac Address: %s " % (ip, macaddr))
        oq.task_done()


#Place ip addresses into in queue
for ip in ips:
    in_queue.put(ip)

#spawn pool of ping threads
for i in range(num_ping_threads):

    worker = Thread(target=pinger, args=(i, in_queue, out_queue))
    worker.setDaemon(True)
    worker.start()


#spawn pool of arping threads
for ip in ips:
    in_queue.put(ip)

for i in range(num_ping_threads):
    worker = Thread(target=pinger, args=(i, in_queue, out_queue))
    worker.setDaemon(True)
    worker.start()

for i in range(num_arp_threads):
    worker = Thread(target=arping, args=(i, out_queue))
    worker.setDaemon(True)
    worker.start()


print("Main Thread Waiting")
in_queue.join()
out_queue.join()

print("Done")

# oq.put(ip) 写入队列oq

# 多队列多线程,ping ip地址并反查出mac

# 3+3 双队列,成功的流入输出队列,打印,查arp,默认值为None,没结果显示默认值
# 还是没解决线程冲突的问题, join只能保证线程结束后继续运行,不能保证几个线程同时运行

# re用的很漂亮,结果分割为列表,分别匹配正则,捕获结果有点问题,用的时候再调试

# 2段处理,是个很好的demo,用之前补上锁,是否有必要?
# arping 只能本地用,阿里做处理了,无反馈, -w 也不行 