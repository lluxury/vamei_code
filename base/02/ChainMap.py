# Accessing Values
import collections
a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
m = collections.ChainMap(a,b)
print('Individual Values')
print('a = {}'.format(m['a']))
print('b = {}'.format(m['b']))
print('c = {}'.format(m['c']))
# print('Keys = {}' ).format(list(m.keys()))
print('Keys = {}'.format(list(m.keys())))
# print('Values = {}'.format(list(m.values)))
print('Values = {}'.format(list(m.values())))

print('Items:')
for k,v in m.items():
    print('{} = {}'.format(k, v))

print('"d" in m: {}'.format(('d' in m)))
# 先有a的c,所以b的c就不存在了,次序



x=format(list(m.keys()))
# "['a', 'c', 'b']"
type(x)
# str


# Reordering
import collections
a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
m = collections.ChainMap(a, b)
print(m.maps)
print('c = {}\n'.format(m['c']))
# c = C
m.maps = list(reversed(m.maps))
print(m.maps)
print('c = {}'.format(m['c']))
# c = D
# 看来确实是和次序有关的



# Updating Values
import collections
a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
m = collections.ChainMap(a, b)
print('Before: {}'.format(m['c']))
a['c'] = 'E'
print('After: {}'.format(m['c']))
# After : ChainMap({'c': 'E', 'a': 'A'}, {'c': 'D', 'b': 'B'})



m1 = collections.ChainMap(a, b)
m2 = m1.new_child()
# m2 before: ChainMap({}, {'c': 'C', 'a': 'A'}, {'c': 'D', 'b':'B'})
m2['c'] = E
# m2 after: ChainMap({'c': 'E'}, {'c': 'C', 'a': 'A'}, {'c': 'D','b': 'B'})
# 要注意, 容易失误

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
c = {'c': 'E'}

m1 = collections.ChainMap(a, b)
m2 = m1.new_child(c)

print('m1["c"] = {}'.format(m1['c']))
print('m2["c"] = {}'.format(m2['c']))

# m2 = collections.ChainMap(c, *m1.maps)
#                          方法,队列?
# m1["c"] = C
# m2["c"] = E                         