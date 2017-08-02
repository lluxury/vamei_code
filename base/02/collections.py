# class collections.ChainMap(*maps)
# maps
# new_child(m=None)
# parents

# ChainMap
from collections import ChainMap
m1 = {'color': 'red', 'user': 'guest'}
m2 = {'name': 'drfish', 'age': '18'}
cm = ChainMap(m1, m2)
print(cm.items())
print(cm.get('name'))
print(cm.get('not'))
m3 = {'data': '1-6'}
#cm = ChainMap.new_child(m3)
cm = cm.new_child(m3)
print(cm.items())

print(cm.parents)
print(cm.parents.parents)
print(cm.parents.parents.parents)
cm.maps
#获取属性


#Counter
from collections import Counter
c = Counter()
c = Counter('hello')
#c = Counter('a':3, 'b':19)
c = Counter({'a':3, 'b':19})
c = Counter(cats=2, dogs=1)
Counter({'cats':2, 'dogs':1})
c['birds']
del c['cats']
#更新,新增,删除
c = Counter(a=4, b=2, c=0, d=-2)
list(c.elements())
c.most_common(1)

c = Counter(a=13, b=11)
d = Counter(a=1, b=2)
c.subtract(d)
# Counter({'a': 12, 'b': 9})
c + d
c - d
c & d
c | d
# subtract()方法进行减法后会影响调用方
# &操作表示取两个中数目小的一个（如果只在一个Counter中存在，则结果集中也没有）
# |操作取数目大的,各种操作负数忽略



#deque
from collections import deque
qd = deque('abd')
qd.append('1')
qd.appendleft('-11')
qd.popleft()
qd.extendleft("hello")
# deque(['o', 'l', 'l', 'e', 'h', 'a', 'b', 'd', '1'])
# x反转后前插列表
dq = deque("12345")
dq.rotate(2)
# deque(['4', '5', '1', '2', '3'])
dq.rotate(-4)
# 回转



#defaultdict
import collections
def default_factory():
    return 'default value'
d = collections.defaultdict(default_factory, foo='bar')
print('d:', d)
print('foo =>', d['foo'])
print('bar =>', d['bar'])
# 2个key foo和bar,比类的方法舒服一点

from collections import defaultdict
d = defaultdict(int)
d['a']
d = defaultdict(dict)
d['a']
# d = defaultdict()
# 没有预设类型一样报错




#namedtuple
from collections import namedtuple
#Point = nametuple("Point",['x', 'y'])
Point = namedtuple("Point",['x', 'y'])
p = Point(1,2)
p.x
p.y
# 每个位置设置别名?
p._asdict()
d = {'x':11, 'y':22}
Point(**d)
# 转为有序字典
p
p._fields
p._replace(x=10)
# 获取所有域,修改相应值



#OrderedDict
from collections import OrderedDict
fruit=(('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1))
d = dict(fruit)
d.popitem()
# 乱序弹出
od = OrderedDict(fruit)
od.popitem()
# od.popitem(last=True)
# 先入先出
od = OrderedDict(fruit)
od.move_to_end('apple')
od.move_to_end('pear',False)
# True时移到末尾，False移到开头