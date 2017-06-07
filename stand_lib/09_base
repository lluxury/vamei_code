
ps -o pid,pgid,ppid,comm | cat
# 25244 25244 25204 su
# 25246 25246 25244 bash
# 26208 26208 25246 ps
# 26209 26208 25246 cat

# 每个进程都会属于一个进程组(process group)，每个进程组中可以包含多个进程
# 进程组会有一个进程组领导进程 (process group leader)，领导进程的PID 成为进程组的ID (process group ID, PGID)，以识别进程组

# ps和cat都是bash的子进程
# 领导进程可以先终结。此时进程组依然存在，并持有相同的PGID，直到进程组中最后一个进程终结

#ps,cat都是08组的,组长是ps, 2者的爸爸都是46


# 在shell支持工作控制(job control)的前提下，多个进程组还可以构成一个会话 (session)
# bash(Bourne-Again shell)支持工作控制，而sh(Bourne shell)并不支持

# 会话是由其中的进程建立的，该进程叫做会话的领导进程(session leader)
# 会话领导进程的PID成为识别会话的SID(session ID)会话中的每个进程组称为一个工作(job)
# 会话可以有一个进程组成为会话的前台工作(foreground)，而其他的进程组是后台工作(background)

# 每个会话可以连接一个控制终端(control terminal)。当控制终端有输入输出时，都传递给该会话的前台进程组
# 由终端产生的信号，比如CTRL+Z， CTRL+\，会传递到前台进程组

# 会话的意义在于将多个工作囊括在一个终端，并取其中的一个工作作为前台，来直接接收该终端的输入输出以及终端信号 其他工作在后台运行。
#一般都会放后台,因为前台有持续输出的时候,无法操作

ping localhost > log &
#[1] 26229 #是PGID
ps -o pid,pgid,ppid,sid,tty,comm	#进程,组,爹,会话,tty,命令
kill -SIGTERM -10141	#在PGID前面加-来表示是一个PGID而不是PID 
kill -SIGTERM %1   #发送给工作1
#其实一直没注意到

cat > log &
fg %1
#输入完成后，按下CTRL+D来通知shell输入结束

