map(function, iterable, ...)

#正常
def add100(x):
    return x+100

hh = [11,22,33]
map(add100,hh)
#[111, 122, 133]


#三发
def abc(a, b, c):
    return a*10000 + b*100 + c

list1 = [11,22,33]
list2 = [44,55,66]
list3 = [77,88,99]
map(abc,list1,list2,list3)
#[114477, 225588, 336699]
#实质为列操作


list1 = [11,22,33]
map(None,list1)

#[11, 22, 33]
list1 = [11,22,33]
list2 = [44,55,66]
list3 = [77,88,99]
map(None,list1,list2,list3)
#[(11, 44, 77), (22, 55, 88), (33, 66, 99)]



#假设
map(f, iterable)
#基本上等于：
[f(x) for x in iterable]

#一元成立
def add100(x):
    return x + 100

list1 = [11,22,33]
map(add100,list1)
#[101, 102, 103]

[add100(i) for i in list1]
#[101, 102, 103]
#真

def abc(a, b, c):
    return a*10000 + b*100 + c
list1 = [11,22,33]
list2 = [44,55,66]
list3 = [77,88,99]
map(abc,list1,list2,list3)
#[114477, 225588, 336699]

#[abc(a,b,c) for a in list1 for b in list2 for c in list3]
#错误结果
[abc(a,b,c) for a,b,c in zip(list1,list2,list3)]
#正确结果 偏转用法

将三个list看做矩阵的话：
11 22 33
44 55 66
77 88 99
map()只做了列上面的运算，而列表推导（也就是嵌套for循环）做了笛卡尔乘积
#原理
