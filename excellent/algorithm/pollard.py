def primefactors(n):
    '''Generate all prime factors of n.'''
    f = 2
    while f * f <=n:
        while not n % f:
            yield f
            n //=f
        f+=1

    if n > 1:
        yield n

print(max(primefactors(600851475143)))

# Pollard p-1
# Pollard ρ
# 有空走一次推到,算法需要再了解多一点,有余数不执行while
# 是没有余数迭代,所以,能除的时候直接除 36/2,不能除的时候,f+1
# 还是不太会作yield