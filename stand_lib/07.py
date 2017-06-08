#信号 进程传递消息 整数
#由内核或其他进程产生
# 当该进程执行系统调用时，在系统调用完成后退出内核时，都会确认,如果有信号，进程会执行对应该信号的操作(signal action,signal disposition

kill -SIGCONT  27397
#信号传给进程

# 信号处理 (signal disposition)
# 在上面的例子中，所有的信号都采取了对应信号的默认操作。但这并不绝对。当进程决定执行信号的时候，有下面几种可能：
# 无视(ignore)信号，信号被清除，进程本身不采取任何特殊的操作
# 默认(default)操作。每个信号对应有一定的默认操作。比如上面SIGCONT用于继续进程。
# 自定义操作。也叫做获取 (catch) 信号。执行进程中预设的对应于该信号的操作

# 信号机制; generate, deliver, pending, blocking
# signal action/dispositon; ignore, default action, catch signal

import signal
print signal.SIGALRM
print signal.SIGCONT
#使用信号

# signal包的核心是使用signal.signal()函数来预设(register)信号处理函数，如下所示：
singnal.signal(signalnum, handler)
# signalnum为某个信号，handler为该信号的处理函数。#我们在信号基础里提到，进程可以无视信号，可以采取默认操作，还可以自定义操作。
# 当handler为signal.SIG_IGN时，信号被无视(ignore)
# 当handler为singal.SIG_DFL，进程采取默认操作(default)
# 当handler为一个函数名时，进程采取函数中定义的操作


import signal
# Define signal handler function
def myHandler(signum, frame):
    print('I received: ', signum)

# register signal.SIGTSTP's handler 
signal.signal(signal.SIGTSTP, myHandler)
signal.pause()
print('End of Signal Demo')
#使用例子,运行时等待
#通过按下CTRL+Z向该进程发送SIGTSTP信号,运行myHandler函数
#也可以通过kill 发信号给进程号 (父进程)
kill -SIGTSTP 26149


#signal.alarm() #被用于在一定时间之后(超时)，向进程自身发送SIGALRM信号
import signal
# Define signal handler function
def myHandler(signum, frame):
    print("Now, it's the time")
    exit()

# register signal.SIGALRM's handler 
signal.signal(signal.SIGALRM, myHandler)
signal.alarm(5)
while True:
    print('not yet')
#使用例子,超时退出

os.kill(pid, sid)
os.killpg(pgid, sid)
#程序发信号




