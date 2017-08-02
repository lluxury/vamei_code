#冒泡排序(bubble sort)
# def short_buble_sort(a_list):
def short_bubble_sort(a_list):
    exchanges = True
    pass_num = len(a_list) -1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                # temp = a_list[i]
                # a_list[i] = a_list[i + 1]
                # a_list[i + 1] = temp
                a_list[i],a_list[i+1] = a_list[i+1], a_list[i]
        pass_num = pass_num - 1

# if __name__ = '__main__':
if __name__ == '__main__':
    a_list=[20, 40, 30, 90, 50, 80, 70, 60, 110, 100]
    short_bubble_sort(a_list)
    print(a_list)

# 函数,交换设真,索引值
# 当索引大于0并交换为真
# 交换假, 遍历列表
# 相邻比较,交换真,对调,索引递减





#选择排序(selection sort)
def selection_sort(a_list):
    for fill_slot in range(len(a_list)-1, 0, -1):
        pos_of_max =0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
    a_list[fill_slot],a_list[pos_of_max]=a_list[pos_of_max],a_list[fill_slot]

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(a_list)
print(a_list)

# 按队列长构造索引,倒序,最大位置0
# 正常遍历,如果某值大于最大,位置替换
# 就是找第1,找第2....为啥要倒序的原因就在这
# 每次索引是个固定值,只要获得当次最大值位置互换就好





#插入排序(insertion sort)
def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position -1] > current_value:
            a_list[position] = a_list[position -1]
            position = position -1
        a_list[position] = current_value


def insertion_sort_binarysearch(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        low = 0
        high = index - 1
        while low <= high:
            mid =(low + high)/2
            if a_list[mid] > current_value:
                high = mid - 1
            else:
                low = mid + 1

        while position > low:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value

a_list = [54, 26, 93, 15, 77, 31, 44, 55, 20]
insertion_sort(a_list)
print(a_list)
insertion_sort_binarysearch(a_list)
print(a_list)
# TypeError: list indices must be integers or slices, not float
# 遍历,当前值为索引1的值, 当位置>0,并且前位置>当前值
# 较小值抹掉,索引前移到0,当前值更新, 其实是替换
# 每次小排序,算了这个算法不想看

# http://javayhu.me/blog/2014/05/07/python-data-structures---c2-sort/



