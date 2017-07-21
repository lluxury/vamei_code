import threading

maxs = 10

threadLimiter = threading.BoundedSemaphore(maxs)

class test(threading.Thread):
    """docstring for test"""
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        threadLimiter.acquire()

        try:
            print("code one")
        except Exception as e:
            pass
        finally:
            threadLimiter.release()

for i in range(100):
    cur = test()
    cur.start()

for i in range(100):
    cur.join()

#控制多纯种并发为10