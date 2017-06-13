
# 装饰器(decorator)是一种高级Python语法。装饰器可以对一个函数、方法或者类进行加工
# 在Python闭包中，函数对象作为某一个函数的返回结果也是一种加工

# 用于加工函数和方法这样的可调用对象(callable object，这样的对象定义有__call__方法), 及加工类

# get square sum
def square_sum(a, b):
    return a**2 + b**2

# get square diff
def square_diff(a, b):
    return a**2 - b**2

print(square_sum(3, 4))
print(square_diff(3, 4))
#求平方和,平方差

# modify: print input
# get square sum
def square_sum(a, b):
    print("intput:", a, b)
    return a**2 + b**2

# get square diff
def square_diff(a, b):
    print("input", a, b)
    return a**2 - b**2

print(square_sum(3, 4))
print(square_diff(3, 4))
#需求
#只是说明,没有input语句


def decorator(F):
    def new_F(a, b):
        print("input", a, b)
        return F(a, b)
    return new_F

# get square sum
@decorator
def square_sum(a, b):
    return a**2 + b**2

# get square diff
@decorator
def square_diff(a, b):
    return a**2 - b**2

print(square_sum(3, 4))
print(square_diff(3, 4))
#装饰器写法
#定义装饰器F, 定义函数new_F,函数功能及返回调用,反回函数

# 在函数square_sum和square_diff定义之前调用@decorator，
# 实际上将square_sum或square_diff传递给decorator，并将decorator返回的新的可调用对象赋给原来的函数名(square_sum或square_diff)
# 相当于
square_sum = decorator(square_sum)
square_sum(3, 4)
#f本来就是个函数啊!!

# 含参的装饰器
# 上例 @decorator，该装饰器默认它后面的函数是唯一的参数, F就是square_sum()的形参
# 装饰器的语法允许调用decorator时，提供其它参数，比如@decorator(a)

# a new wrapper layer
def pre_str(pre=''):
    
    # old decorator
    def decorator(F):
        def new_F(a, b):
            print(pre + "input", a, b)
            return F(a, b)
        return new_F
    return decorator

# get square sum
@pre_str('^_^')
def square_sum(a, b):
    return a**2 + b**2

# get square diff
@pre_str('T_T')
def square_diff(a, b):
    return a**2 - b**2

print(square_sum(3, 4))
print(square_diff(3, 4))
#就是调用装饰器时带了不同参数
# 在外面再写一层函数,连装饰器本身也返回

# 对原有装饰器的一个函数封装，并返回一个装饰器 可以将它理解为一个含有环境参量的闭包
# 使用@pre_str('^_^')调用的时候，Python能够发现这一层的封装，并把参数传递到装饰器的环境中
square_sum = pre_str('^_^') (square_sum)
#调的装饰器是最外层的封装, 调的参数还是需要 ' '
#场景,参数处理人名之类可变的量,装饰器处理不变的量

# 在Python 2.6以后，装饰器被拓展到类。一个装饰器可以接收一个类，并返回一个类，从而起到加工类的效果

def decorator(aClass):
    class newClass:
        
        def __init__(self, age):
            self.total_display   = 0
            self.wrapped         = aClass(age)
        
        def display(self):
            self.total_display += 1
            print("total display", self.total_display)
            self.wrapped.display()
    return newClass

@decorator
class Bird:
    
    def __init__(self, age):
        self.age = age
    
    def display(self):
        print("My age is",self.age)

eagleLord = Bird(5)
for i in range(3):
    eagleLord.display() 
# 在decorator中，返回了一个新类newClass。
# 在新类中，记录了原来类生成的对象（self.wrapped），并附加了新的属性total_display，用于记录调用display的次数。
# 同时更改了display方法。
# 通过修改，Bird类可以显示调用display的次数了。

#类的2个变量: self.total_display是整型, self.wrapped是实例  
##执行,先跑一次,不进函数, 27调用,8函数,15返回,23执行,需要方法跳14调用方法, 被装饰的类,原有的参数就这样用掉了?? 貌似!!
#所谓改写,有了装饰器,类里的同名函数已经不起作用了!!

# 装饰器的核心作用是name binding。这种语法是Python多编程范式的又一个体现?






