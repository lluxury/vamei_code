import threading

def run(n):
    print("code two")
threads = []

#creat threading
for i in range(10):
    t = threading.Thread(target=run,args=(i, ))
    threads.append(t)

    #run thread
    t.start()


#block thread
for i in threads:
    t.join()
    while True:
        if (len(threading.enumerate()) <5 ):
            break




#线程池
import threadpool

def ThreadFun(arg1, arg2)
    pass

def main():
    device_list = [object1, object2, object3,....,objectn]
    task_pool = threadpool.threadpool(8)
    request_list = []

for device in device_list:
    request_list.append(threadpool.makeRequests(ThreadFun,[((device, ), {})]))

    map(task_pool.putRequest, request_list)
    task_pool.task_pool()

if __name__=="__main__":
    main()

#这个线程池的代码写的怪怪的,有机会再更新成独立的吧
