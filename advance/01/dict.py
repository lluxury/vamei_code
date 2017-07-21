a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
a == b == c == d == e
#true
len(d)
d['one']


class Counter(dict):
    def __missing__(self, key):
        return 0
c = Counter()
# c['red'] 0
c['red'] += 1
# c['red'] 1 
#定义了 __missing__方法,补了默认值



e.get('one','xx')
#有就是one的值 ,没有就回xx

e.fromkeys('one') 
# {'e': None, 'n': None, 'o': None}
# 不是很理解

e.get('one','xx')
1

e.items()
# dict_items([('two', 2), ('one', 1), ('three', 3)])

e.keys()
# dict_keys(['two', 'one', 'three'])

e.popitem()
# ('two', 2)    f[0]为'two'
# 随机的 显示对应,可以赋给变量,但类型是tuple
f=[a.popitem()]
f=dict([a.popitem()])
g.update(f)
# 生成列表,字典,融合字典的方法
# 或者生成列表 g=g+f 再 dict(g)转换

e.pop('one')
# 1

e.setdefault('one')
# {'one': None, 'three': 3}

e.update(a)
# {'one': 1, 'onx': None, 'three': 3, 'two': 2}
# 同key的都被洗掉,不同的留存,没有的补上


dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()
values =dishes.values()

#iteration
n = 0
for val in values:
    n += val
print(n)

# keys and values are iterated over in the same order
list(keys)
list(values)

keys & {'eggs', 'bacon', 'salad'}
keys ^ {'sausage', 'juice'}


