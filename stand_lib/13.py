
迭代器/循环器(iterator)
# 调用循环器的next()方法 ,(__next__()方法，在Python 3.x中)
# 所有的对象遍历穷尽，循环器将举出StopIteration错误

# 在for i in iterator结构中，循环器每次返回的对象将赋予给i，直到循环结束
# 使用iter()内置函数，我们可以将诸如表、字典等容器变为循环器
for i in iter([2, 4, 5, 6]):
    print(i)

# import the tools
from itertools import *

无穷循环器
count(5, 2)     #从5开始的整数循环器，每次增加2，即5, 7, 9, 11, 13, 15 ...
cycle('abc')    #重复序列的元素，既a, b, c, a, b, c ...
repeat(1.2)     #重复1.2，构成无穷循环器，即1.2, 1.2, 1.2, ...

repeat也可以有一个次数限制:
repeat(10, 5)   #重复10，共重复5次

函数式工具
函数式的处理 map(), filter(), reduce()函数
itertools包含类似的工具。这些函数接收函数作为参数，并将结果返回为一个循环器

from itertools import *

rlt = imap(pow, [1, 2, 3], [1, 2, 3])

for num in rlt:
    print(num)

# imap函数 该函数与map()函数功能相似，只不过返回的不是序列，而是一个循环器

starmap(pow, [(1, 1), (2, 2), (3, 3)])
# pow将依次作用于表的每个tuple

# ifilter函数与filter()函数类似，只是返回的是一个循环器。
ifilter(lambda x: x > 5, [2, 3, 5, 6, 7]
# 将lambda函数依次作用于每个元素，如果函数返回True，则收集原来的元素。6, 7

ifilterfalse(lambda x: x > 5, [2, 3, 5, 6, 7])
# 与上面类似，但收集返回False的元素。2, 3, 5

takewhile(lambda x: x < 5, [1, 3, 6, 7, 1])
# 当函数返回True时，收集元素到循环器。一旦函数返回False，则停止。1, 3

dropwhile(lambda x: x < 5, [1, 3, 6, 7, 1])
# 当函数返回False时，跳过元素。一旦函数返回True，则开始收集剩下的所有元素到循环器。6, 7, 1

组合工具
# 通过组合原有循环器，来获得新的循环器。
chain([1, 2, 3], [4, 5, 7])      # 连接两个循环器成为一个。1, 2, 3, 4, 5, 7

product('abc', [1, 2])   # 多个循环器集合的笛卡尔积。相当于嵌套循环        

for m, n in product('abc', [1, 2]):
    print m, n

permutations('abc', 2)   # 从'abcd'中挑选两个元素，比如ab, bc, ... 将所有结果排序，返回为新的循环器。
# 注意，上面的组合分顺序，即ab, ba都返回。

combinations('abc', 2)   # 从'abcd'中挑选两个元素，比如ab, bc, ... 将所有结果排序，返回为新的循环器。
# 注意，上面的组合不分顺序，即ab, ba的话，只返回一个ab。

combinations_with_replacement('abc', 2) # 与上面类似，但允许两次选出的元素重复。即多了aa, bb, cc

groupby()
# 将key函数作用于原循环器的各个元素。根据key函数结果，将拥有相同函数结果的元素分到一个新的循环器。每个新的循环器以函数返回结果为标签
def height_class(h):
    if h > 180:
        return "tall"
    elif h < 160:
        return "short"
    else:
        return "middle"

friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]

friends = sorted(friends, key = height_class)
for m, n in groupby(friends, key = height_class):
    print(m)
    print(list(n))

# 一群人的身高作为循环器。我们可以使用这样一个key函数: 
# 如果身高大于180，返回"tall"；如果身高底于160，返回"short";中间的返回"middle"。最终，所有身高将分为三个循环器，即"tall", "short", "middle"
# groupby的功能类似于UNIX中的uniq命令。分组之前需要使用sorted()对原循环器的元素，根据key函数进行排序，让同组元素先在位置上靠拢

compress('ABCD', [1, 1, 1, 0])  # 根据[1, 1, 1, 0]的真假值情况，选择第一个参数'ABCD'中的元素。A, B, C
islice()                        # 类似于slice()函数，只是返回的是一个循环器
izip()                          # 类似于zip()函数，只是返回的是一个循环器。


#具体用例,自行匹配
from itertools import *
timeit [0 for i in xrange(10000)]
timeit list(repeat(0,10000))

it=chain(xrange(5),"abc")
list(it)
list(combinations("abcd",2))
list(permutations("abcd",2))
#list(permutations("abcd",3))
it=combinations_with_replacement("abcd",2)
list(it)
it=compress("abcde",[True,False,True])
list(it)
list(ifilter(lambda x: x%2, range(10)))
list(ifilterfalse(lambda x: x%2, range(10)))
list(dropwhile(lambda x: x<5, [1,4,6,4,1]))
list(takewhile(lambda x: x<5, [1,4,6,4,1]))

test = chain.from_iterable('ABCDEF')
test.next()
test.next()

test=count(10000)
test.next()
test.next()

test=cycle(range(3))
test.next()
test.next()

from itertools import *
list(islice('ABCDEFG', 2))
list(islice('ABCDEFG', 2,4))
list(islice('ABCDEFG', 2,None))
list(islice('ABCDEFG', 2,None,2))
list(izip('ABCD', 'xy'))
list(izip_longest('ABCD', 'xy', fillvalue='-'))
list(product('ABCD', 'xy'))
list(product(range(2), repeat=3))
