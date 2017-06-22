
def auth_args(auth_type):
    def auth(func):
        def war(*args, **kwargs):
            if auth_type == 'file':
                name = input("username: ")
                pwd = int(input("password: "))
                if name == 'xyy' and pwd == 123:
                    print("log successful!")
                    func(*args, **kwargs)
                else:
                    print("login error!")
            elif auth_type == 'sql':
                print('error typing')
        return war
    return auth

@auth_args(auth_type='sql')
def write():
    print('welcome to home!')

@auth_args(auth_type='file')
def test():
    print('only test')

write()
test()

#带参数版,可以做多项目验证之类的应用,拦截等
#参数可以在装饰器里用