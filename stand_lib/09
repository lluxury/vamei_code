
uid gid
# 用户信息保存在/etc/passwd中 组信息保存在/etc/group中
# 当我们向对某个文件进行操作的时候，我们需要在进程中运行一个程序，在进程中对文件打开，并进行读、写或者执行的操作
# 我们需要将用户的权限传递给进程，以便进程真正去执行操作

# 以用户的身份登录，并在shell中运行如下命令：
$cat test.txt
# 整个过程中我们会有两个进程，一个是shell本身(2256)，一个是shell复制自身，再运行/bin/cat (9913)
# 第二个进程总共对文件系统进行了两次操作，一次是执行(x)文件/bin/cat，另外一次是读取(r)文件test.txt
ls -l /bin/cat
ls -l test.txt

# 尽管用户拥有相应的权限，但我们发现，真正做工作的是进程9913 让这个进程得到相应的权限
每个进程会维护有如下6个ID
真实身份: real UID,       real GID    登录身份
有效身份: effective UID,  effective GID 检查身份
存储身份：saved UID,      saved GID  

# 当进程fork的时候，真实身份和有效身份都会复制给子进程。大部分情况下，真实身份和有效身份都相同
# Linux的最小特权(least priviledge)的原则
# 一个进程最开始的有效身份是真实身份，但运行到中间的时候，需要以其他的用户身份读入某些配置文件，然后再进行其他的操作
# 为了防止其他的用户身份被滥用，我们需要在操作之前，让进程的有效身份变更回来成为真实身份。这样，进程需要在两个身份之间变化。

# 当我们将一个程序文件执行成为进程的时候，该程序文件的拥有者(owner)和拥有组(owner group)可以被，存储成为进程的存储身份
# 在随后进程的运行过程中，进程就将可以选择将真实身份或者存储身份复制到有效身份，以拥有真实身份或者存储身份的权限
# 并不是所有的程序文件在执行的过程都设置存储身份的
# 需要这么做的程序文件会在其九位(bit)权限的执行位的x改为s。这时，这一位(bit)叫做set UID bit或者set GID bit

# 通常使用chmod来修改set-UID bit和set-GID bit
chmod 4700 file
# 最前面一位用于处理set-UID bit/set-GID bit 它可以被设置成为4/2/1以及或者上面数字的和
# 4表示为set UID bit, 2表示为set GID bit，1表示为sticky bit 
# 必须要先有x位的基础上，才能设置s位

real/effective/saved UID/GID
saved UID/GID bit
最小权限 原则


#os包中有查询和修改进程信息
uname() #返回操作系统相关信息
umask() #设置该进程创建文件时的权限mask

get*() 查询 (*由以下代替)
    uid, euid, resuid, gid, egid, resgid #：权限相关，其中resuid主要用来返回saved UID #相关介绍见Linux用户与“最小权限”原则
    pid, pgid, ppid, sid                 #：进程相关

put*() 设置 (*由以下代替)
    euid, egid #： 用于更改euid，egid。
    uid, gid  #： 改变进程的uid, gid。只有super user才有权改变进程uid和gid (意味着要以$sudo python的方式运行Python)。
    pgid, sid #： 改变进程所在的进程组(process group)和会话(session)。

getenviron()#：获得进程的环境变量
setenviron()#：更改进程的环境变量

import os
print(os.getuid())
print(os.getgid())

#当我们写一个Python脚本后，我们实际运行的是python这个解释器，而不是Python脚本文件
# 对比C，C语言直接运行由C语言编译成的执行文件。我们必须更改python解释器本身的权限来运用saved UID机制，然而这么做又是异常危险的??

ls -l /usr/bin/python
# -rwxr-xr-x root root

#修改权限以设置set UID和set GID位
sudo chmod 6755 /usr/bin/python
# -rwsr-sr-x root root

#运行脚本
import os
print(os.getresuid())
# (1000, 0, 0) UID，EUID，saved UID 获得超级权限
sudo chmod 0755 /usr/bin/python

# http://www.faqs.org/faqs/unix-faq/faq/part4/section-7.html 

