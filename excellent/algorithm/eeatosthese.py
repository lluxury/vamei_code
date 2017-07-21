def countPrimes(n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    # print(primes)
    
    for i in range(2, int(n ** 0.5) + 1):
        # print(i)
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return (primes)

#print(sum(countPrimes(87654321)))
# 求质数的个数

# 安全判断,小于3的直接否
# 全为真,前2个位置人工设为假
# i在2到开方n+1里面
# 如果对应值为真, 切片2*2:n:2 对应点为假* 队列的长度
# 目前支持8千万
# 使用了列表,资源消耗巨大

def sushu(n):
    result = []
    for x in range(2,n+1):
        for y in range(2,x):
            if x % y == 0:
                break
        else:
            result.append(x)
    return result  
#print(sushu(31))  

# 常规解法,需要400+步骤
# 但是占用的内存量并不是很大,只是时间长,指数级的差别

