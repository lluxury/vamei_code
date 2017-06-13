# Python一切皆对象，但同时，Python还是一个多范式语言(multi-paradigm),
# 不仅可以使用面向对象的方式来编写程序，还可以用面向过程的方式来编写相同功能的程序(还有函数式、声明式等)。
# Python的多范式依赖于Python对象中的特殊方法(special method)。

# 特殊方法名的前后各有两个下划线。特殊方法又被成为魔法方法(magic method)
# 当对象中定义了特殊方法的时候，Python也会对它们有“特殊优待”。
# 定义了__init__()方法的类，会在创建对象的时候自动执行__init__()方法中的操作

Python的运算符是通过调用对象的特殊方法实现的
'abc' + 'xyz'	#实质是
'abc'.__add__('xyz')

# 在Python中，两个对象是否能进行加法运算，首先就要看相应的对象是否有__add__()方法。
# 一旦相应的对象有__add__()方法，即使这个对象从数学上不可加，我们都可以用加法的形式，来表达obj.__add__()所定义的操作。

# Python不强制用户使用面向对象的编程方法。用户可以选择自己喜欢的使用方式(比如选择使用+符号，还是使用更加面向对象的__add__()方法)。

(1.8).__mul__(2.0)
True.__or__(False)


#内置函数
# 与运算符类似，许多内置函数也都是调用对象的特殊方法。
len([1,2,3])      # 实际上做的是
[1,2,3].__len__()

(-1).__abs__()
(2.3).__int__()

#表(list)元素引用
li = [1, 2, 3, 4, 5, 6]
print(li[3])
#原理
li = [1, 2, 3, 4, 5, 6]
print(li.__getitem__(3))

li.__setitem__(3, 0)
{'a':1, 'b':2}.__delitem__('a')
# 此方法是__delitem__（self,key），即对原字典对应键的值进行删除，而获得新的列表


#函数

# 在Python中，函数也是一种对象。任何一个有__call__()特殊方法的对象都被当作是函数。
class SampleMore(object):
    def __call__(self, a):
        return a + 5

add = SampleMore()     # A function object
print(add(2))          # Call function    
map(add, [2, 4, 5])    # Pass around function object

dir(SampleMore)

# Python的许多语法都是基于其面向对象模型的封装, xx方法,貌似可以自己造