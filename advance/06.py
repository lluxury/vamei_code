# 迭代器
l = ['a','b','c','d','e']
i = l.__iter__()

while True:
    try:
        print(i.__next__())
#except StopIteration:
    except StopIteration:
        break



l = ['a','b','c','d','e']
i = 0
while i < len(l):
    print(l[i])
    i += 1


l = ['a','b','c','d','e']
for i in l:
    print(i)


l = ['a','b','c','d','e']
for i in range(len(l)):
    print(l[i])

#目前习惯第3种,最简单



dic = {'a':1,'b':2,'c':3}
i = dic.__iter__()

while True:
    try:
        print(i.__next__())
    except StopIteration:
        break




with open('test.py', 'r+', encoding='utf8') as f:
    a = f.__iter__()
    while True:
        try:
            print(a.__next__(),end='')
        except StopIteration:
            break



from collections import Iterable,Iterator

s = "xyyp"
l = ['a','b','c']
t = (1,2,3,4)
d = {"s":1,"a":4}
f = open('test.py')
#前4个都有迭代方法,但不是迭代器

print(isinstance(s,Iterable))
print(isinstance(l,Iterable))
print(isinstance(t,Iterable))
print(isinstance(d,Iterable))
print(isinstance(f,Iterable))
print(isinstance(s,Iterator))
print(isinstance(l,Iterator))
print(isinstance(t,Iterator))
print(isinstance(d,Iterator))
print(isinstance(f,Iterator))

# iterable —— 只实现了__iter__的对象；
# iterator —— 同时实现了__iter__和__next__方法的对象

accounts_iterator = iter(accounts)
(next(accounts_iterator)).account_name
#转为迭代器?
