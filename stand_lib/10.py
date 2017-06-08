threading和multiprocessing
# multiprocessing包是Python中的多进程管理包 它可以利用multiprocessing.Process对象来创建一个进程 该进程可以运行在Python程序内部编写的函数
# multiprocessing包中也有Lock/Event/Semaphore/Condition类
# multiprocessing的很大一部份与threading使用同一套API，只不过换到了多进程的情境

注意
# 在UNIX平台上，当某个进程终结之后，该进程需要被其父进程调用wait，否则进程成为僵尸进程(Zombie) 有必要对每个Process对象调用join()方法 (实际上等同于wait)
# 对于多线程来说，由于只有一个进程，所以不存在此必要性
# multiprocessing提供了threading包中没有的IPC(比如Pipe和Queue)，效率上更高。应优先考虑Pipe和Queue
# 避免使用Lock/Event/Semaphore/Condition等同步方式 (因为它们占据的不是用户进程的资源)

多进程应该避免共享资源
# 在多线程中，我们可以比较容易地共享资源，比如使用全局变量或者传递参数
# 在多进程情况下，由于每个进程有自己独立的内存空间，以上方法并不合适。此时我们可以通过共享内存和Manager的方法来共享资源
# 但这样做提高了程序的复杂度，并因为同步的需要而降低了程序的效率

Process.PID#中保存有PID，如果进程还没有start()，则PID为None
# 各个线程和进程都做一件事：打印PID。但问题是，所有的任务在打印的时候都会向同一个标准输出(stdout)输出。这样输出的字符会混合在一起，无法阅读
# 使用Lock同步，在一个任务输出完成之后，再允许另一个任务输出，可以避免多个任务同时向终端输出


# Similarity and difference of multi thread vs. multi process
# Written by Vamei

import os
import threading
import multiprocessing

# worker function
def worker(sign, lock):
    lock.acquire()
    print(sign, os.getpid())
    lock.release()

# Main
print('Main:',os.getpid())

# Multi-thread
record = []
lock  = threading.Lock()
for i in range(5):
    thread = threading.Thread(target=worker,args=('thread',lock))
    thread.start()
    record.append(thread)

for thread in record:
    thread.join()

# Multi-process
record = []
lock = multiprocessing.Lock()
for i in range(5):
    process = multiprocessing.Process(target=worker,args=('process',lock))
    process.start()
    record.append(process)

for process in record:
    process.join()


#join()阻塞主进程结束
#Linux多线程 管道PIPE和消息队列message queue
# multiprocessing包中有Pipe类和Queue类来分别支持这两种IPC机制
# Pipe可以是单向(half-duplex)，也可以是双向(duplex) 我们通过mutiprocessing.Pipe(duplex=False)创建单向管道 (默认为双向)

# Multiprocessing with Pipe
# Written by Vamei

import multiprocessing as mul

def proc1(pipe):
    pipe.send('hello')
    print('proc1 rec:',pipe.recv())

def proc2(pipe):
    print('proc2 rec:',pipe.recv())
    pipe.send('hello, too')

# Build a pipe
pipe = mul.Pipe()

# Pass an end of the pipe to process 1
p1   = mul.Process(target=proc1, args=(pipe[0],))
# Pass the other end of the pipe to process 2
p2   = mul.Process(target=proc2, args=(pipe[1],))
p1.start()
p2.start()
p1.join()
p2.join()


# 这里的Pipe是双向的 Pipe对象建立的时候，返回一个含有两个元素的表
# 每个元素代表Pipe的一端(Connection对象) 我们对Pipe的某一端调用send()方法来传送对象，在另一端使用recv()来接收



# Queue与Pipe相类似，都是先进先出的结构。但Queue允许多个进程放入，多个进程从队列取出对象
# Queue使用mutiprocessing.Queue(maxsize)创建，maxsize表示队列中可以存放对象的最大数量

# Written by Vamei
import os
import multiprocessing
import time
#==================
# input worker
def inputQ(queue):
    info = str(os.getpid()) + '(put):' + str(time.time())
    queue.put(info)

# output worker
def outputQ(queue,lock):
    info = queue.get()
    lock.acquire()
    print (str(os.getpid()) + '(get):' + info)
    lock.release()
#===================
# Main
record1 = []   # store input processes
record2 = []   # store output processes
lock  = multiprocessing.Lock()    # To prevent messy print
queue = multiprocessing.Queue(3)

# input processes
for i in range(10):
    process = multiprocessing.Process(target=inputQ,args=(queue,))
    process.start()
    record1.append(process)

# output processes
for i in range(10):
    process = multiprocessing.Process(target=outputQ,args=(queue,lock))
    process.start()
    record2.append(process)

for p in record1:
    p.join()

queue.close()  # No more object will come, close the queue

for p in record2:
    p.join()

# 一些进程使用put()在Queue中放入字符串，这个字符串中包含PID和时间 另一些进程从Queue中取出，并打印自己的PID以及get()的字符串


Process, Lock, Event, Semaphore, Condition

Pipe, Queue


