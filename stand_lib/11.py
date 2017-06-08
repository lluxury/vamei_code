
进程池 (Process Pool)可以创建多个进程 准备执行任务(程序)
import multiprocessing as mul

def f(x):
    return x**2

pool = mul.Pool(5)
rel  = pool.map(f,[1,2,3,4,5,6,7,8,9,10])
print(rel)

# 创建了一个容许5个进程的进程池 (Process Pool)Pool运行的每个进程都执行f()函数
# 我们利用map()方法，将f()函数作用到表的每个元素上。这与built-in的map()函数类似，只是这里用5个进程并行处理

apply_async(func,args)  #从进程池中取出一个进程执行func，args为func的参数。它将返回一个AsyncResult的对象，你可以对该对象调用get()方法以获得结果。
close()  #进程池不再创建新的进程
join()   #wait进程池中的全部进程。必须对Pool先调用close()方法才能join

共享资源
# 应该尽量避免多进程共享资源。多进程共享资源必然会带来进程间相互竞争 而这种竞争又会造成race condition，我们的结果有可能被竞争的不确定性所影响

# 信号可以看作一种粗糙的进程间通信(IPC, interprocess communication)的方式，用以向进程封闭的内存空间传递信息

管道(PIPE)机制#。在Linux文本流中，可以使用管道将一个进程的输出和另一个进程的输入连接起来，从而利用文件操作API来管理进程间通信
# 传统IPC (interprocess communication)。我们主要是指消息队列(message queue)，信号量(semaphore)，共享内存(shared memory) 
# 这些IPC的特点是允许多进程之间共享资源，这与多线程共享heap和global data相类似
# 由于多进程任务具有并发性 (每个进程包含一个进程，多个进程的话就有多个线程)，所以在共享资源的时候也必须解决同步的问题

# 通过一个文件交流也是一种IPC,便是硬盘太慢

# 原理上，管道利用fork机制建立 最开始的时候，两个连接在同一个进程Process 1上 当fork复制进程的时候，会将这两个连接也复制到新的进程(Process 2)
# 随后，每个进程关闭自己不需要的一个连接  Process 1关闭从PIPE来的输入连接，Process 2关闭输出到PIPE的连接 PIPE完成

# 由于基于fork机制，所以管道只能用于父进程和子进程之间，或者拥有相同祖先的两个子进程之间 (有亲缘关系的进程之间)
# 为了解决这一问题，Linux提供了FIFO方式连接进程。FIFO又叫做命名管道(named PIPE)

 FIFO #(First in, First out)为一种特殊的文件类型，它在文件系统中有对应的路径
# 当一个进程以读(r)的方式打开该文件，而另一个进程以写(w)的方式打开该文件，那么内核就会在这两个进程之间建立管道，所以FIFO实际上也由内核管理，不与硬盘打交道
# 管道本质上是一个先进先出的队列数据结构，最早放入的数据被最先读出来
# 从而保证信息交流的顺序。FIFO只是借用了文件系统来为管道命名。写模式的进程向FIFO文件中写入，而读模式的进程从FIFO文件中读出
# FIFO的好处在于我们可以通过文件的路径来识别管道

传统IPC
# 并不使用文件操作的API。对于任何一种IPC来说，你都可以建立多个连接，并使用键值(key)作为识别的方式
# 可以在一个进程中中通过键值来使用的想要那一个连接 (比如多个消息队列，而我们选择使用其中的一个)
# 键值可以通过某种IPC方式在进程间传递(比如说我们上面说的PIPE，FIFO或者写入文件)，也可以在编程的时候内置于程序中

# 在几个进程共享键值的情况下，这些传统IPC非常类似于多线程共享资源的方式
# semaphore与mutex类似，用于处理同步问题 semaphore就是一个计数锁 
# 它允许被N个进程获得。当有更多的进程尝试获得semaphore的时候，就必须等待有前面的进程释放锁
# 当N等于1的时候，semaphore与mutex实现的功能就完全相同 一个semaphore会一直存在在内核中，直到某个进程删除它

# 共享内存与多线程共享global data和heap类似 一个进程可以将自己内存空间中的一部分拿出来，允许其它进程读写
# 当使用共享内存的时候，我们要注意同步的问题。我们可以使用semaphore同步，也可以在共享内存中建立mutex或其它的线程同步变量来同步
# 由于共享内存允许多个进程直接对同一个内存区域直接操作，所以它是效率最高的IPC方式

# 消息队列(message queue)与PIPE相类似。它也是建立一个队列，先放入队列的消息被最先取出
# 消息队列允许多个进程放入消息，也允许多个进程取出消息。每个消息可以带有一个整数识别符(message_type
# 某个进程从队列中取出消息的时候，可以按照先进先出的顺序取出，也可以只取出符合某个识别符的消息(有多个这样的消息时，同样按照先进先出的顺序取出)
# 消息队列与PIPE的另一个不同在于它并不使用文件API
# 一个队列不会自动消失，它会一直存在于内核中，直到某个进程删除该队列

PIPE, FIFO

semaphore, message queue, shared memory; key

共享内存

# modified from official documentation
import multiprocessing

def f(n, a):
    n.value   = 3.14
    a[0]      = 5

num   = multiprocessing.Value('d', 0.0)
arr   = multiprocessing.Array('i', range(10))

p = multiprocessing.Process(target=f, args=(num, arr))
p.start()
p.join()

print num.value
print arr[:]

# 我们在主进程的内存空间中创建共享的内存，也就是Value和Array两个对象 
# 对象Value被设置成为双精度数(d), 并初始化为0.0。而Array则类似于C中的数组，有固定的类型(i, 也就是整数)
# 在Process进程中，我们修改了Value和Array对象。回到主程序，打印出结果

Manager
# Manager对象类似于服务器与客户之间的通信 (server-client)，与Internet上的活动很类似。用一个进程作为服务器，建立Manager来真正存放资源
# 其它的进程可以通过参数传递或者根据地址来访问Manager，建立连接后，操作服务器上的资源
import multiprocessing

def f(x, arr, l):
    x.value = 3.14
    arr[0] = 5
    l.append('Hello')

server = multiprocessing.Manager()
x    = server.Value('d', 0.0)
arr  = server.Array('i', range(10))
l    = server.list()

proc = multiprocessing.Process(target=f, args=(x, arr, l))
proc.start()
proc.join()

print(x.value)
print(arr)
print(l)

# Manager利用list()方法提供了表的共享方式。实际上可以利用dict()来共享词典，Lock()来共享threading.Lock
# (注意，共享的是threading.Lock，而不是进程的mutiprocessing.Lock。后者本身已经实现了进程共享)等 这样Manager就允许我们共享更多样的对象

Pool

Shared memory, Manager