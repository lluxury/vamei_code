def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print (b)
        a, b = b, a + b
        n+=1
print(fab(5))

# 普通写法,没有返回值,其他函数无法使用


def fab(max):
    n, a, b= 0, 0, 1
    L=[]
    while n < max:
        L.append(b)
        a, b = b, a+b
        n+=1
    return L

for n in fab(5):
    print(n)

# 可以获得数列的版本,用队列输出返回
# 缺点随max的增加list内存使用增加, 昨天遇到了


class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    #def next(self):
    def __next__(self):
        if self.n <self.max:
            r = self.b
            self.a, self.b = self.b, self.a +self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

for n in Fab(5):
    print(n)

# 通过重写类的方法,重写了__init__, __iter__, __next__的方法
# 但是我没看到哪里调用next方法,是自动么? 回答如下
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法
# 实现一个__iter__()方法，该方法返回一个迭代对象，python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值
# 实例本身就是迭代对象，故返回自己

# __iter__()返回 0, 1, 5, 0 ,并执行next.
# r获得 self.b的值 1, 函数返回值为1,输出1
# 继续调用__next__()方法,变量为 1, 1, 5, 1   a和n发生了变化, 上次一a和n就变化了,没输出,直接拿起来用
# r获得 self.b的值, 随后self.b发生了变化,但输出的r还是旧值1,除a,n 同样变化了, n没有变成5,还会继续调用
# 关于r的设置是因为,本来就是要反馈第二个数,后面的操作只是为下一次做准备?

# 只使用当前值,大大节省资源,倒是太繁琐




def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        #print b
        a, b = b, a + b
        n+=1

for n in fab(5):
    print(n)

# 调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象 f,f有方法 f.__next__()
# 在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值
# 就是输出值,像print一样,然后再循环,并跳过yield继续执行
# 下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，
# 于是函数继续执行，直到再次遇到 yield
# 再给个输出值,像print b一样,然后再循环,并跳过yield继续执行

# 一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，但不会执行任何函数代码，
# 直到对其调用 next()才开始执行,（for 循环中会自动调用 next()）.
# 每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行
# 一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值
# 比起用类的实例保存状态来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰

# 以上2段描述都正确



# return的作用
# 在一个 generator function 中，如果没有 return，则默认执行至函数完毕，如果在执行过程中 return，则直接抛出 StopIteration 终止迭代
# 在 for 循环里，无需处理 StopIteration 异常，循环会正常结束

def read_file(fpath):
    BLOCK_SIZE =1024
    while open(fpath, 'rb') as f:
        while True:
            block =f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return
# 避免读太多内容,内存溢出,读到yield时返回当前值,并继续执行后续, 并循环
# 迭代器是一个对象，而生成器是一个函数? 给函数加了yield就成了生成器?
# 迭代器就是有一个 next() 方法的对象, 而不是通过索引来计数




# 在迭代可变对象的时候修改它们并不是个好主意
for eachURL in allURLs:  
    if not eachURL.startswith(‘http://’):  
        allURLs.remove(eachURL) # YIKES!!   x
RuntimeError: dictionary changed size during iteration
# 一个序列的迭代器只是记录你当前到达第多少个元素, 所以如果你在迭代时改变了元素, 更新会立即反映到你所迭代的条目上.
# 在迭代字典的 key 时, 你绝对不能改变这个字典. 使用字典的 keys() 方法是可以的


# 创建迭代器
iter(obj)  
# 检查传递的参数是不是一个序列,从索引0开始迭代
iter(func, sentinel)
# 如果是传递两个参数给 iter() , 它会重复地调用 func , 直到迭代器的下个值等于sentinel
# 使用类的方法,见开头


# reversed() 内建函数将返回一个反序访问的迭代器. enumerate() 内建函数同样也返回迭代器
# 两个新的内建函数, any() 和 all()
# myDict.iterkeys() (通过 keys 迭代), 
# myDict.itervalues() (通过 values 迭代), 
# myDicit.iteritems() (通过 key/value 对来迭代)
# itertools 模块
