
python - m pdb hello_world.py
python - m cProfile hello_world.py

# ipython
import pdb
import hello
pdb.run(‘hello.test()’)

#断点 (ide使用较多)
if __name__ == "__main__":
a = 1
import pdb
pdb.set_trace()
b = 2
c = a + b
print(c)


# 调试命令 进入提示符后
# h   帮助
# l 列表
# b 断点 b77
#        b 全部断点
#   条件断点 condition 77 a==3

# cl    清除断点
#   disable/enable，禁用/激活断点

# n   下一行,不进函数
# s   下一行,进入函数

# c   正常运行直到断点
# j 跳转到指定行

# a 打印参数
# p   打印变量  p hl
# !   改变变量  ! hl

# q   退出

# w   Print a stack trace
# d   Move the current frame one level down in the stack trace
# u   Move the current frame one level up in the stack trace (to an older
# frame).


# l, b77, c, p hl, q
# j 4, !hl = 'xx'
