
#Traversal遍历
def walk(G, s, S=set()):
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        #for v in G[u].defference(P, S):
        for v in G[u].difference(P, S):
            Q.add(v)
            P[v] = u
    return P

def some_graph():
    a, b, c, d, e, f, g, h = range(8)
    N = [
        [b, c, d, e, f],    # a
        [c, e],             # b
        [d],                # c
        [e],                # d
        [f],                # e
        [c, h],          # f
        [f, h],             # g
        [f, g]              # h
    ]
    return N

G = some_graph()
for i in range(len(G)): G[i] = set(G[i])
print (list(walk(G,0))) #[0, 1, 2, 3, 4, 5, 6, 7]

# 第二个函数构造了一个图,然后跑了walk函数,构图方法
# 图的连通分量是图的一个最大子图，在这个子图中任何两个节点之间都是相互可达的(忽略边的方向)
# 构造函数,从s出发,前任,队列,s没有前任,从s出发,当队列存在,队里随机选一个,新节点? 访问,记录,返回轨迹
# difference函数的使用，参数可以是多个，调用后返回的集合中的元素在各个参数中都不存在

# 图函数,a-h 赋值1-7,再造8个列表,各含不同字母对应的数字,表示连接关系 a是int,N是2阶列表
# for语句把获得图的定点数,然后把list转为set,防重复? 到此图构成完毕

# 调用walk函数,参数G和0,0表示起点s,既从0点开始遍历
# 设P,Q 2个变量,P[0]为空,没前任,集合Q为0点, u表示当前顶点
# 当Q存在时,弹出Q给u,队列存在给出顶点 
# G[0]的difference(P, S) 不在集合里的元素,还是用法不会 

# 当Q在0点时,v获得1...5,Q获得1-5,再赋给P,字典1-5 都为0点,(Q表示可以出发的点 0顶点) 
# Q依次弹出,但没有新的发现,直到5点,发现6,7, 记入字典,都为5点
# 1,2,3,4,5可以过就直接走,6过不去就从7过去

# 单点,无方向图,获得连通分量




#全部的连通分量
def components(G):
    comp = []
    seen = set()
    for u in G:
        if u in seen:continue
        C = walk(G, u)
        seen.update(C)
        comp.append(C)
    return comp

G = {
    0: set([1, 2]),
    1: set([0, 2]),
    2: set([0, 1]),
    3: set([4, 5]),
    4: set([3, 5]),
    5: set([3, 4])
    }

print ([list(sorted(C)) for C in components(G)])  #[[0, 1, 2], [3, 4, 5]]

# G是一个字典,记录点和连接
# u表示各个顶点,也是字典里的key
# seen表示去过的点,comp表示结果
# c = walk(G,u) 带入图顶点计算,更新点,追加结果

# 欧拉回路和：经过图中的所有边一次，然后回到起点
# 哈密顿回路: 经过图中的所有顶点一次，然后回到起点





#深度优先搜索(DFS)
def rec_dfs(G, s, S=None):
    if S is None: S = set()
    S.add(s)
    for u in G[s]:
        if u in S: continue
        #rec_defs(G, u ,S)
        rec_dfs(G, u ,S)
    return S

def some_graph():
    a, b, c, d, e, f, g, h = range(8)
    N = [
        [b, c, d, e, f],    # a
        [c, e],             # b
        [d],                # c
        [e],                # d
        [f],                # e
        [c, g, h],          # f
        [f, h],             # g
        [f, g]              # h
    ]
    return N




def iter_dfs(G,s):
    S, Q = set(), []
    Q.append(s)
    #While Q:
    while Q:
        u = Q.pop()
        if u in S: continue
        S.add(u)
        Q.extend(G[u])
        yield u
 
G = some_graph()
for i in  range(len(G)): G[i] = set(G[i])
print(list(iter_dfs(G,0))) #[0,5,7,5,2,3,4,1]

# 普通写法和递归写法, 调用自己和中断继续,为什么结果不一样




def traverse(G, s, qtype=set):
    S, Q = set(), qtype()
    Q.add(s)
    while Q:
        u = Q.pop()
        if u in S: continue
        S.add(u)
        for v in G[u]:
            Q.add(v)
        yield u


G = some_graph()
class stack(list):
    add = list.append
print(list(traverse(G, 0, stack)))
# 通用的遍历函数, qtype为队列类型, 如stack?
# 所有的节点 u 的后继节点 v 的区间都在节点 u 的区间内部，
# 如果节点 v 不是节点 u 的后继，那么两个节点的区间不相交，这就是“括号定理







#topological Sorting Based on Depth-first Search
#def def_topsort(G):
def dfs_topsort(G):
    S, res = set(), []
    def recurse(u):
        if u in S: return
        S.add(u)
        for v in G[u]:
            recurse(v)
        res.append(u)
    for u in G:
        recurse(u)
    res.reverse()
    return res

G = {'a': set('bf'), 'b': set('cdf'), 'c': set('d'), 'd': set('ef'), 'e':
        set('f'), 'f': set()}
print(dfs_topsort(G))

# G是一个集合组成的字典, S,res表示历史和结果
# 定义了一个内部程序,可以吃到G和res等变量
# 如里在历史,返回, 否则加入历史,遍历u点的值
# 用其值代入内部程序,加入结果
# 遍历G的u点, 带入程序,完成的反转,输出

# a,recurese(a),判断,添加入S,遍历v in G[u],带入程序
# b加入历史,遍历其值f,f没有返回值,不代入,结果f点加res,一条倒底了
# 返回,代入b的第二个值d,继续代入,最后e加入res...

# 拓扑排序刚好是节点的完成时间f[v]降序排列



#深度优先,个人测试版,结果不唯一啊,没写完成么,据说不考虑方向
#topological Sorting Based on Depth-first Search
#def def_topsort(G):
def dfs_topsort(G):
    S, res = set(), []
    def recurse(u):
        if u in S: return
        S.add(u)
        for v in G[u]:
            recurse(v)
        res.append(u)
    for u in G:
        recurse(u)
    res.reverse()
    return res

G = {
    'undershorts': set(('pants','shoes')),
    'pants':set(('belt','shoes','undershorts')),
    'shoes': set(('socks','undershorts','pants')),
    'socks': set(('shoes',)),
    'watch':set(), 
    'belt': set(('jacket','pants','shirt')),
    'shirt':set(('belt','tie')),
    'tie':set(('jacket','shirt')),
    'jacket': set(('tie','belt'))
    }
print(dfs_topsort(G))





#Breadth-First Search
from collections import deque

def bfs(G, s):
    P, Q = {s: None}, deque([s])
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P: continue
            P[v] = u
            Q.append(v)
    return P

def some_graph():
    a, b, c, d, e, f, g, h = range(8)
    N = [
        [b, c, d, e, f],    # a
        [c, e],             # b
        [d],                # c
        [e],                # d
        [f],                # e
        [c, g, h],          # f
        [f, h],             # g
        [f, g]              # h
    ]
    return N

G = some_graph()
print (bfs(G, 0))
# Q是双向队列,先拿到参数0, 当Q存在时,弹出,遍历值,
# 如果在字典,跳过,否则u写入字典P[v],并把v加入队列Q
# 当执行完后,返回P,就是结果 dict

# list可以很好地充当stack，但是充当queue则性能很差，所以使用deque






#强连通分量
#前面的分量是不考虑边的方向的，如果我们考虑边的方向，而且得到的最大子图中，任何两个节点都能够沿着边可达，那么这就是一个强连通分量
# 对G运行Dfs,得到完成时间f[v], 
# 得到原图的转置图GT
# 对GT运行DFS,主循环按f[v]降序访问
# 输出深度优先的每棵树,就是强连通分支
def tr(G):
    GT = {}
    for u in G: GT[u] = set()
    for u in G:
        for v in G[u]:
            GT[v].add(u)
    return GT



def scc(G):
    GT= tr(G)
    sccs, seen = [], set()
    for u in dfs_topsort(G):
        if u in seen: continue
        C = walk(GT, u, seen)
        seen.update(C)
        sccs.append(C)
    return sccs

from string import ascii_lowercase
def parse_graph(s):
    # print zip(ascii_lowercase, s.split("/"))
    # [('a', 'bc'), ('b', 'die'), ('c', 'd'), ('d', 'ah'), ('e', 'f'), ('f', 'g'), ('g', 'eh'), ('h', 'i'), ('i', 'h')]
    G = {}
    for u , line in zip(ascii_lowercase, s.split("/")):
        G[u] = set(line)
    return G

G = parse_graph('bc/die/d/ah/f/g/eh/i/h')
print(list(map(list, scc(G))))
#[['a', 'c', 'b', 'd'], ['e', 'g', 'f'], ['i', 'h']]

# 结论可以回归,但是消化大约需要时间了,遍历函数,深度排序,强连接
# 获得所有点,获得图,