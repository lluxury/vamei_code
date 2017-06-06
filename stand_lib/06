
#subprocess还提供了一些管理标准流(standard stream)和管道(pipe)的工具，从而在进程间使用文本通信

# 使用subprocess包中的函数创建子进程的时候，要注意:
# 在创建子进程之后，父进程是否暂停，并等待子进程运行。
# 函数返回什么
# 当returncode不为0时，父进程如何处理

subprocess.call()
# 父进程等待子进程完成

subprocess.check_call()
# 完成返回0 ，如果returncode不为0，举出错误subprocess.CalledProcessError

subprocess.check_output()
# 父进程等待子进程完成
# 返回子进程向标准输出的输出结果

import subprocess
rc = subprocess.call(["ls","-l"])

import subprocess
out = subprocess.call("cd ..", shell=True)
#shell的内建命令必须使用这种方式运行,比如 cd ..,相当于先起一个shell再运行

#以上都是基于Popen()的封装(wrapper)

import subprocess
child = subprocess.Popen(["ping","-c","5","www.google.com"])
print("parent process")
#不使用封闭时,父进程 会先执行print

import subprocess
child = subprocess.Popen(["ping","-c","5","www.google.com"])
child.wait()
print("parent process")
#对比结果
child.poll()           # 检查子进程状态
child.kill()           # 终止子进程
child.send_signal()    # 向子进程发送信号
child.terminate()      # 终止子进程
#child.pid

# child.stdin
# child.stdout
# child.stderr

import subprocess
child1 = subprocess.Popen(["ls","-l"], stdout=subprocess.PIPE)
child2 = subprocess.Popen(["wc"], stdin=child1.stdout,stdout=subprocess.PIPE)
out = child2.communicate()
print(out)
#和管道运行的结果有些不一样,要注意
# subprocess.PIPE实际上为文本流提供一个缓存区。child1的stdout将文本输出到缓存区，随后child2的stdin从该PIPE中将文本读取走
# child2的输出文本也被存放在PIPE中，直到communicate()方法从PIPE中读取出PIPE中的文本

# communicate()是Popen对象的一个方法，该方法会阻塞父进程，直到子进程完成

import subprocess
child = subprocess.Popen(["cat"], stdin=subprocess.PIPE)
child.communicate("lluxury")
#也可以用做给子进程输入