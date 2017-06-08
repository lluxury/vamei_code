import threading
import time

count = 1

class KissThread(threading.Thread):
    def run(self):
        global count
        print ("Thread # %s:  Pretending to do stuff" % count)
        count += 1
        time.sleep(2)
        print ("done with stuff")

for t in range(5):
    KissThread().start()


#global 的写法怪怪的, 有没有其他写法
#  是一样的,不过赋值一般会放在函数下面,主程序上面

#没有.join, 作用及影响?
#引用了现有类,写了一个方法,
#没有设置锁,有插队的现象,如何改进

# Thread # 1: Pretending to do stuff
#  Thread # 1: Pretending to do stuff
# Thread # 3: Pretending to do stuff
