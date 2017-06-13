

# Python一切皆对象(object)，每个对象都可能有多个属性(attribute)。Python的属性有一套统一的管理方案。

# 对象的属性可能来自于其类定义，叫做类属性(class attribute)
# 类属性可能来自类定义自身，也可能根据类定义继承来的
# 一个对象的属性还可能是该对象实例定义的，叫做对象属性(object attribute)

# 对象的属性储存在对象的__dict__属性中。__dict__为一个词典，键为属性名，对应的值为属性本身

class bird(object):
    feather = True

class chicken(bird):
    fly = False
    def __init__(self, age):
        self.age = age

summer = chicken(2)

print(bird.__dict__)
print(chicken.__dict__)
print(summer.__dict__)
# chicken类继承自bird类，而summer为chicken类的一个对象

# Python中的属性是分层定义的，比如这里分为object/bird/chicken/summer这四层
# 当需要调用某个属性的时候，Python会一层层向上遍历，直到找到那个属性
# (某个属性可能出现再不同的层被重复定义，Python向上的过程中，会选取先遇到的那一个，也就是比较低层的属性定义)

# 当我们有一个summer对象的时候，分别查询summer对象、chicken类、bird类以及object类的属性，
# 就可以知道summer对象所有的__dict__，就可以找到通过对象summer可以调用和修改的所有属性了

summer.__dict__['age'] = 3
print(summer.__dict__['age'])

summer.age = 5
print(summer.age)

summer.fly = True
print(summer.fly)
#True
#上级的属性,确实可以用到

print(summer.__class__)
print(dir(summer))
print(chicken.__base__)
#bird
print(dir(chicken))
# 如果只有一个对象，而不知道它的类以及其他信息的时候，可以利用__class__属性找到对象的类，然后调用类的__base__属性来查询父类)


#特性
# 同一个对象的不同属性之间可能存在依赖关系。当某个属性被修改时，我们希望依赖于该属性的其他属性也同时变化。
# 这时，我们不能通过__dict__的方式来静态的储存属性。

class bird(object):
    feather = True

class chicken(bird):
    fly = False

    def __init__(self, age):
        self.age = age
    
    def getAdult(self):
        if self.age > 1.0: return True
        else: return False
    adult = property(getAdult)   # property is built-in

summer = chicken(2)

print(summer.adult)
summer.age = 0.5
print(summer.adult)
# 我们为chicken类增加一个特性adult。当对象的age超过1时，adult为True；否则为False：



class num(object):
    
    def __init__(self, value):
        self.value = value
    
    def getNeg(self):
        return -self.value
    
    def setNeg(self, value):
        self.value = -value
    
    def delNeg(self):
        print("value also deleted")
        del self.value
    
    neg = property(getNeg, setNeg, delNeg, "I'm negative")

x = num(1.1)
print(x.neg)

x.neg = -22
print(x.value)
print(num.neg.__doc__)
del x.neg
# 特性使用内置函数property()来创建。property()最多可以加载四个参数。前三个参数为函数，分别用于处理查询特性、修改特性、删除特性。
# 最后一个参数为特性的文档，可以为一个字符串，起说明作用。

# num为一个数字，而neg为一个特性，用来表示数字的负数。当一个数字确定的时候，它的负数总是确定的；
# 修改一个数的负数时，它本身的值也应该变化。这两点由getNeg和setNeg来实现。
# 而delNeg表示的是，如果删除特性neg，那么应该执行的操作是删除属性value。
# property()的最后一个参数("I'm negative")为特性negative的说明文档

#还是看不懂, 不过先记录一下吧


# 特殊方法__getattr__
# 用__getattr__(self, name)来查询即时生成的属性
# 当查询一个属性时，如果通过__dict__方法无法找到该属性，那么Python会调用对象的__getattr__方法，来即时生成该属性

class bird(object):
    feather = True

class chicken(bird):
    fly = False
    
    def __init__(self, age):
        self.age = age
    
    def __getattr__(self, name):
        if name == 'adult':
            if self.age > 1.0: return True
            else: return False
        else: raise AttributeError(name)

summer = chicken(2)
print(summer.adult)

summer.age = 0.5
print(summer.adult)

print(summer.male)
#查询, __dict__()没值, 调用 __getattr__方法?
#主动触发 AttributeError


__getattribute__  #特殊方法，用于查询任意属性
__getattr__  #只能用来查询不在__dict__系统中的属性
__setattr__(self, name, value) __delattr__(self, name) #可用于修改和删除属性 可用于任意属性


#生成属性的其他方式
# descriptor(descriptor类实际上是property()函数的底层 property()实际上创建了一个该类的对象

# __dict__分层存储属性 每一层的__dict__只存储该层新增的属性。子类不需要重复存储父类中的属性 
# 即时生成属性是值得了解的概念