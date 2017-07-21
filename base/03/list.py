A = [[None] *2 ] *3
#[[None, None], [None, None], [None, None]]

A[0][0]=5
#[[5, None], [5, None], [5, None]]
# * 并不是建造拷贝,相与是映射关系,要注意


A = [None] * 3
for i in range(3):
    A[i] = [None] * 2


w, h = 2, 3
A = [[None] * w for i in range(h)]
A[0][0]=5
# [[5, None], [None, None], [None, None]]
# 两种解决方案,不过还是感觉坑


a_tuple = (['boo'], 'bar')
a_tuple[0] += ['item']  #正常是不行的
# ['boo', 'item'] 会报错,但是添加上了


a_list = []
a_list += [1]
# a_list [1]  列表值的增加
result = a_list.__iadd__([1])
a_list = result


list1 = ["what", "I'm", "sorting", "by"]
list2 = ["something", "else", "to", "sort"]
pairs = zip(list1, list2)
pairs = sorted(pairs)
type(pairs)
result = [x[1] for x in pairs]

result = []
for p in pairs: result.append(p[1])
