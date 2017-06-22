class Account():
    def __init__(self,
        account_name,
        account_type,
        account_cost,
        return_amount=0):
        self.account_name = account_name # 账户名
        self.account_type = account_type # 账户类型
        self.account_cost = account_cost # 月结费用
        self.return_amount = return_amount # 返还金额

accounts = [
Account("张三", "年费用户", 450.00, 50),
Account("李四", "月结用户", 100.00),
Account("杨不悔", "月结用户", 190.00, 25),
Account("任我行", "月结用户", 70.00, 10),
Account("凌未风", "年费用户", 400.00, 40)
]


class AccountIterator():
    def __init__(self, accounts):
        self.accounts = accounts # 账户集合
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.accounts):
            raise StopIteration("到头了...")
        else:
            self.index += 1
            return self.accounts[self.index-1] 


accounts_iterator = iter(accounts)
print ((next(accounts_iterator)).account_name)
print ((next(accounts_iterator)).account_cost)

#注意用法,各属性需要1次性调出,再运行游标已经变了

accounts_iterator = AccountIterator(accounts)
print(next(accounts_iterator).account_name)

for a in accounts_iterator:
    print(a.account_name)   


# 转换迭代器与自建迭代器
# 迭代与遍历
