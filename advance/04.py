
# 闭包(closure)是函数式编程的重要的语法结构
# 函数式编程是一种编程范式 (而面向过程编程和面向对象编程也都是编程范式)
# 在面向过程编程中，见到过函数(function)；在面向对象编程中，见过对象(object)
# 闭包是一种组织代码的结构，提高代码的可重复使用性(reusability)

# 不同的语言实现闭包的方式不同 Python以函数对象为基础

# 函数对象的作用域
# 函数对象有其存活的范围，也就是函数对象的作用域 
# 函数对象是使用def语句定义的，函数对象的作用域与def所在的层级相同

def line_conf():
    def line(x):
        return 2*x+1
    print(line(5))   # within the scope


line_conf()
print(line(5))       # out of the scope
# 在line_conf函数的隶属范围内定义的函数line，就只能在line_conf的隶属范围内调用

# 如果使用lambda定义函数，那么函数对象的作用域与lambda所在的层级相同

# 闭包
# 函数是一个对象，所以可以作为某个函数的返回结果

def line_conf():
    def line(x):
        return 2*x+1
    return line       # return a function object

my_line = line_conf()
print(my_line(5)) 
# line_conf的返回结果被赋给line对象


#引入外部变量
def line_conf():
    b = 15
    def line(x):
        return 2*x+b
    return line       # return a function object

b = 5
my_line = line_conf()
print(my_line(5))
#25 
# line定义的隶属程序块中引用了高层级的变量b，但b信息存在于line的定义之外 (b的定义并不在line的隶属程序块中)
# 我们称b为line的环境变量 事实上，line作为line_conf的返回值时，line中已经包括b的取值(尽管b并不隶属于line)

# line所参照的b值是函数对象定义时可供参考的b值，而不是使用时的b值 (我的理解是定义了5,进函数又定义了一次??)

# 一个函数和它的环境变量合在一起，就构成了一个闭包(closure)
# 在Python中，所谓的闭包是一个包含有环境变量取值的函数对象


def line_conf():
    b = 15
    def line(x):
        return 2*x+b
    return line       # return a function object

b = 5
my_line = line_conf()
print(my_line.__closure__)
print(my_line.__closure__[0].cell_contents)
# 环境变量取值被保存在函数对象的__closure__属性中

# __closure__里包含了一个元组(tuple)。这个元组中的每个元素是cell类型的对象。
# 第一个cell包含的就是整数15，也就是创建闭包时的环境变量b的取值


def line_conf(a, b):
    def line(x):
        return a*x + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5), line2(5))
# 函数line与环境变量a,b构成闭包

# line_conf的参数a,b说明了这两个环境变量的取值
# 只需要变换参数a,b，就可以获得不同的直线表达函数 闭包也具有提高代码可复用性的作用

# line函数定义一种广泛意义的函数。这个函数的一些方面已经确定(必须是直线)，但另一些方面(比如a和b参数待定)
# 根据line_conf传递来的参数，通过闭包的形式，将最终函数确定下来

# 闭包与并行运算
# 闭包有效的减少了函数所需定义的参数数目。这对于并行运算来说有重要的意义
# 在并行运算的环境下，我们可以让每台电脑负责一个函数，然后将一台电脑的输出和下一台电脑的输入串联起来。最终，我们像流水线一样工作?








