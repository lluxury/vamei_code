from threading import Thread
import subprocess
import Queue

num_threads = 3
queue = Queue.Queue()
ips = ["223.5.5.5", "223.6.6.6", "114.114.114.114", "8.8.8.8"]


def pinger(i, q):
    '''PING SUBNET'''
    while True:
        ip = q.get()
        print("Thread %s: Pinging %s" % (i, ip))
        ret = subprocess.call("ping -c 1 %s" % ip,
                              shell=True,
                              stdout=open('/dev/null', 'w'),
                              stderr=subprocess.STDOUT)
        if ret == 0:
            print("%s: is alive" % ip)
        else:
            print("%s: is not respond" % ip)
        q.task_done()

for i in range(num_threads):
    worker = Thread(target=pinger, args=(i, queue))
    worker.setDaemon(True)
    worker.start()

for ip in ips:
    queue.put(ip)

print("Main Thread Waiting")
queue.join()
print("Done")

#版本是老了,修了很多bug, Queue*2

# 线程,队列 ,从队列中取出一个地址,由线程执行
# ping无限循环,线程不会死亡,守护线程
# 一个缓冲池,三个线程等告诉绑定, 元素放入队列
# queue.join() 调用join导致程序主线程等待,直到队列为空
#线程不是队列, 参数才是队列, 写的比较绕,感觉像官版

# Queue.get([block[, timeout]]) 获取队列，timeout等待时间
# Queue.get_nowait() 相当Queue.get(False)
# Queue.put(item) 写入队列，timeout等待时间
# Queue.task_done() 在完成一项工作之后，Queue.task_done() 函数向任务已经完成的队列发送一个信号
# Queue.join() 实际上意味着等到队列为空，再执行别的操作

# 补充
#     Queue.qsize() 返回队列的大小
#     Queue.empty() 如果队列为空，返回True,反之False
#     Queue.full() 如果队列满了，返回True,反之False
#     Queue.full 与 maxsize 大小对应

# FIFO队列先进先出：class Queue.Queue(maxsize)
# LIFO类似于堆,即先进后出：class Queue.LifoQueue(maxsize)
# 优先级队列级别越低越先出来：class Queue.PriorityQueue(maxsize)
