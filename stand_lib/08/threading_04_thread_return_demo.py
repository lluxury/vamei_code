import threading


class test(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.tag = 1

    def get_result(self):
        if self.tag == 1:
            return True
        else:
            return False

f = test()
f.start()

while f.isAlive():
    continue

print (f.get_result())

# 输是传出来了,怎么应用
