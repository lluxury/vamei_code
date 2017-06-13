
# 上下文管理器(context manager)是Python2.5开始支持的一种语法，用于规定某个对象的使用范围
# 一旦进入或者离开该使用范围，会有特殊操作被调用 (比如为对象分配或者释放内存)。它的语法形式是 with...as...

#关闭文件
# 打开文件，读写，关闭文件。程序员经常会忘记关闭文件。上下文管理器可以在不需要文件的时候，自动关闭文件。

# without context manager
f = open("new.txt", "w")
print(f.closed)               # whether the file is open
f.write("Hello World!")
f.close()
print(f.closed)


# with context manager
with open("new.txt", "w") as f:
    print(f.closed)
    f.write("Hello World!")

print(f.closed)
#print打印的是逻辑值
# 进入程序块之前调用对象的__enter__()方法，在结束程序块的时候调用__exit__()方法



# customized object

class VOW(object):
    
    def __init__(self, text):
        self.text = text
    
    def __enter__(self):
        self.text = "I say: " + self.text    # add prefix
        return self                          # note: return an object
    
    def __exit__(self,exc_type,exc_value,traceback):
        self.text = self.text + "!"          # add suffix


with VOW("I'm fine") as myvow:
    print(myvow.text)

print(myvow.text)
#定义了2个特殊方法,进入退出时操作,类似pre,post
#进入时加了 I say,退出时加了 !

__exit__() #中有四个参数。当程序块中出现异常(exception)，__exit__()的参数中exc_type, exc_value, traceback用于描述异常。
# 我们可以根据这三个参数进行相应的处理。如果正常运行结束，这三个参数都是None。


# with EXPR as VAR:

VAR = EXPR
VAR = VAR.__enter__()
try:
    BLOCK
finally:
    VAR.__exit__()
