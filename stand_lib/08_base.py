#Linux中的线程也都基于进程

#进程是程序的一个具体实现
ps -eo pid,comm,cmd
#id号,命令,参数 []内核功能,写成系统样子

ps -o pid,ppid,cmd
pstree

#fork通常作为一个函数被调用。这个函数会有两次返回，将子进程的PID返回给父进程，0返回给子进程
# 通常在调用fork函数之后，程序会设计一个if选择结构。
# 当PID等于0时，说明该进程为子进程，那么让它执行某些指令,
#   比如说使用exec库函数(library function)读取另一个程序文件，并在当前的进程空间执行 (使用fork的目的之一: 为某一程序创建进程)；
# 而当PID为一个正整数时，说明为父进程，则执行另外一些指令。由此，就可以在子进程建立之后，让它执行与父进程不同的功能

#在子进程中:
pid = fork() #0

# 当子进程终结时，它会通知父进程，并清空自己所占据的内存，并在内核里留下自己的退出信息(exit code，
# 如果顺利运行，为0；如果有错误或异常状况，为>0的整数)。在这个信息里，会解释该进程为什么退出。
# 父进程在得知子进程终结时，有责任对该子进程使用wait系统调用。这个wait函数能从内核中取出子进程的退出信息，并清空该信息在内核中所占据的空间。
# 如果父进程早于子进程终结，子进程就会成为一个孤儿(orphand)进程。孤儿进程会被过继给init进程，init进程也就成了该进程的父进程。init进程负责该子进程终结时调用wait函数。

# 一个糟糕的程序也完全可能造成子进程的退出信息滞留在内核中的状况（父进程不对子进程调用wait函数），子进程成为僵尸（zombie）进程。当大量僵尸进程积累时，内存空间会被挤占。

#在Linux中，线程只是一种特殊的进程。多个线程之间可以共享内存空间和IO接口, 在UNIX中，进程与线程是有联系但不同的两个东西

程序，进程，PID，内存空间
子进程，父进程，PPID，fork， wait


#全局变量 局部变量
内存空间
Stack		#栈,局部变量
Unused Area
Heap		#堆,动态变量, malloc系统调用,直接开辟
Global Data	#全局变量,固定
Text(instruction codes)	#指令,每一步操作,固定

#栈,以帧为单位,调用会增长,存储该函数的参数,局部变量,返回地址
#调用函数时,控制权由main(),到inner(),inner()处于激活状态,
#位于最下方的栈,和全局一起构成当前环境(context), 正常只能用最下方的栈,先进后出
#函数再调用其它的时候,下面会再有栈,控制转移,返回时,从栈中弹出桢(读取删除),根据返回地址奖控制权给所指向指令

#当程序使用malloc时,堆heap会向上增长,malloc开辟的空间会一直存在,直接free或进程结束,这里是内存泄漏 memory leakage 的源头
#栈和堆会随着进程的运行增大或变小,两者相遇时,再无可用内存,进程会栈溢出 stack overflow ,参见同名网站
#高级语言会自动回收

#除了上面信息,每个进程还要包括一些进程附加信息，包括PID，PPID，PGID 
#内核会为每个进程在内核自己的空间中分配一个变量(task_struct结构体)以保存上述信息 以及接受到的信号

#fork & exec
#当一个程序调用fork的时候，实际上就是将上面的内存空间，包括text, global data, heap和stack，又复制出来一个，构成一个新的进程
#并在内核中为改进程创建新的附加信息, 两者内存相同,只能通过进程的附加信息来区分

#程序调用exec的时候，进程清空自身内存空间的text, global data, heap和stack，
#并根据新的程序文件重建text, global data, heap和stack (此时heap和stack大小都为0)，并开始运行。

#IPC 进程间通信

函数，变量的作用范围，global/local/dynamic variables
global data, text,
stack, stack frame, return address, stack overflow
heap, malloc, free, memory leakage
进程附加信息, task_struct
fork & exec


#典型的UNIX系统都支持一个进程创建多个线程(thread)
#这个程序的整个运行过程中，只有一个控制权的存在
#当函数被调用的时候，该函数获得控制权，成为激活(active)函数，然后运行该函数中的指令。与此同时，其它的函数处于离场状态，并不运行
#单线程程序
#多线程就是允许一个进程内存在多个控制权，以便让多个函数同时处于激活状态，从而让多个函数的操作同时运行

#操作系统一般都有一些系统调用来让你将一个函数运行成为一个新的线程
#正常程序一个栈，只有最下方的帧可被读写,多线程的进程在内存中有多个栈 多个栈之间以一定的空白区域隔开
#每个线程可调用自己栈最下方的帧中的参数和变量，并与其它线程共享内存中的Text，heap和global data区域

#对于多线程来说，由于同一个进程空间中存在多个栈，任何一个空白区域被填满都会导致stack overflow的问题

#多线程相当于一个并发(concunrrency)系统,要解决同步问题

#故障举例
/*mu is a global mutex*/

while (1) {                        /*infinite loop*/
    if (i != 0) i = i -1
    else {
      printf("no more tickets");
      exit();
    }
}
#2条指令之间有时间窗, 其间状态会变化

#在并发情况下，指令执行的先后顺序由内核决定。同一个线程内部，指令按照先后顺序执行，但不同线程之间的指令很难说清除哪一个会先执行
#运行结果依赖执行顺序 造成竞争条件(race condition)
#最常见的解决竞争条件的方法是将原先分离的两个指令构成不可分隔的一个原子操作(atomic operation)，而其它任务不能插入到原子操作中

#多线程同步
#对于多线程程序来说，同步(synchronization)是指在一定的时间内只允许某一个线程访问某个资源

# 互斥锁(mutex)
# 条件变量(condition variable)
# 读写锁(reader-writer lock)

# 互斥锁是一个特殊的变量，它有锁上(lock)和打开(unlock)两个状态。互斥锁一般被设置成全局变量
# 打开的互斥锁可以由某个线程获得。一旦获得，这个互斥锁会锁上，此后只有该线程有权打开。其它想要获得互斥锁的线程，会等待直到互斥锁再次打开的时候

/*mu is a global mutex*/

while (1) {                /*infinite loop*/
  mutex_lock(mu);           /*aquire mutex and lock it, if cannot, wait until mutex is unblocked*/
  if (i != 0) i = i - 1;
  else {
    printf("no more tickets");
    exit();
  }
  mutex_unlock(mu);         /*release mutex, make it unblocked*/
}
#获取mu的可以操作,别的程序等着, 但是有老程序的线程不受影响,要重起程序



# 条件变量是另一种常用的变量。它也常常被保存为全局变量，并和互斥锁合作
/*mu: global mutex, cond: global codition variable, num: global int*/
mutex_lock(mu)

num = num + 1;                      /*worker build the room*/

if (num <= 10) {                     /*worker is within the first 10 to finish*/
    cond_wait(mu, cond);            /*wait*/
    printf("drink beer");
}
else if (num = 11) {                /*workder is the 11th to finish*/
  cond_broadcast(mu, cond);         /*inform the other 9 to wake up*/
}

mutex_unlock(mu);

#我们让工人在装修好房间(num = num + 1)之后，去检查已经装修好的房间数( num < 10 )。由于mu被锁上，所以不会有其他工人在此期间装修房间(改变num的值)。
#如果该工人是前十个完成的人，那么我们就调用cond_wait()函数。
#cond_wait()做两件事情，一个是释放mu，从而让别的工人可以建房。另一个是等待，直到cond的通知。这样的话，符合条件的线程就开始等待。
# 当有通知(第十个房间已经修建好)到达的时候，condwait()会再次锁上mu。线程的恢复运行
#前面十个调用cond_wait()的线程如何得到的通知呢？我们注意到elif if，即修建好第11个房间的人，负责调用cond_broadcast()。这个函数会给所有调用cond_wait()的线程放送通知，以便让那些线程恢复运行

#条件变量特别适用于多个线程等待某个条件的发生。如果不使用条件变量，那么每个线程就需要不断尝试获得互斥锁并检查条件是否发生，这样大大浪费了系统的资源。

#读写锁与互斥锁非常相似。r、RW lock有三种状态: 共享读取锁(shared-read), 互斥写入锁(exclusive-write lock), 打开(unlock)。后两种状态与之前的互斥锁两种状态完全相同。
#一个unlock的RW lock可以被某个线程获取R锁或者W锁。
#如果被一个线程获得R锁，RW lock可以被其它线程继续获得R锁,如果此时有其它线程想要获得W锁，它必须等到所有持有共享读取锁的线程释放掉各自的R锁
# 如果一个锁被一个线程获得W锁，那么其它线程，无论是想要获取R锁还是W锁，都必须等待该线程释放W锁
#多个线程就可以同时读取共享资源。而具有危险性的写入操作则得到了互斥锁的保护


multiple threads, multiple stacks

race condition

mutex, condition variable, RW lock
























