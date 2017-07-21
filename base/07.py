a = 1
def change_integer(a):
    a = a + 1
    return a
print (change_integer(a))   #2
print (a)                   #1


# 将一个整数变量传递给函数，函数对它进行操作，但原整数变量a不发生变化。
# 对于基本数据类型的变量，变量传递给函数后，函数会在内存中复制一个新的变量，从而不影响原来的变量, 值传递

b = [1, 2, 3]
def change_list(b):
    b[0] = b[0] +1
    return b
#print (change_list)
print (change_list(b))      #[2, 2, 3]
print(b)                    #[2, 2, 3]

# 将一个表传递给函数，函数进行操作，原来的表b发生变化。
# 但是对于表来说，表传递给函数的是一个指针，指针指向序列在内存中的位置，
# 在函数中对表的操作将在原有内存中进行，从而影响原有变量, 指针传递


