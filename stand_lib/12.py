
# math包数学函数
# numpy和scipy 数组 及矩阵运算 物理函数
常数
math.e   # 自然常数e
math.pi  # 圆周率pi

此外，math包还有各种运算函数 (下面函数的功能可以参考数学手册)：
math.ceil(x)       # 对x向上取整，比如x=1.2，返回2
math.floor(x)      # 对x向下取整，比如x=1.2，返回1
math.pow(x,y)      # 指数运算，得到x的y次方
math.log(x)        # 对数，默认基底为e。可以使用base参数，来改变对数的基地。比如math.log(100,base=10)
math.sqrt(x)       # 平方根

三角函数: math.sin(x), math.cos(x), math.tan(x), math.asin(x), math.acos(x), math.atan(x)
这些函数都接收一个弧度(radian)为单位的x作为参数。
角度和弧度互换: math.degrees(x), math.radians(x)
双曲函数: math.sinh(x), math.cosh(x), math.tanh(x), math.asinh(x), math.acosh(x), math.atanh(x)
特殊函数： math.erf(x), math.gamma(x)

# 了解伪随机数(psudo-random number)的原理 random.seed(x)
# 来改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed

random.choice(seq)   # 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
random.sample(seq,k) # 从序列中随机挑选k个元素
random.shuffle(seq)  # 将序列的所有元素随机排序

# 下面生成的实数符合均匀分布(uniform distribution)，意味着某个范围内的每个数字出现的概率相等:
random.random()          # 随机生成下一个实数，它在[0,1)范围内。
random.uniform(a,b)      # 随机生成下一个实数，它在[a,b]范围内

# 下面生成的实数符合其它的分布 (你可以参考一些统计方面的书籍来了解这些分布):
random.gauss(mu,sigma)    # 随机生成符合高斯分布的随机数，mu,sigma为高斯分布的两个参数。 
random.expovariate(lambd) # 随机生成符合指数分布的随机数，lambd为指数分布的参数。
# 此外还有对数分布，正态分布，Pareto分布，Weibull分布，可参考下面链接:
# http://docs.python.org/library/random.html

import random
all_people = ['Tom', 'Vivian', 'Paul', 'Liya', 'Manu', 'Daniel', 'Shawn']
random.shuffle(all_people)
for i,name in enumerate(all_people):
    print(i,':'+name)

enumerate #枚举
math.floor(), math.sqrt(), math.sin(), math.degrees()
random.random(), random.choice(), random.shuffle()