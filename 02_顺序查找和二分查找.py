'''
    查找：在一些数据元素中，通过一定的方法找出与给定关键字相同的数据元素的过程

    列表查找（线性查找）：从列表中查找指定元素
        输入：列表，待查找元素
        输出：元素下标(找不到返回None 或者 -1)
    内置列表查找函数：index()


    顺序查找：也叫线性查找，从列表的第一个元素开始，顺序进行搜索，直到找到元素或搜索到列表最后一个元素为止。

    二分查找：从有序列表的初始候选区li[0:n]开始，通过对待查找的值与候选区中间值的比较，可以使候选区减少一半。
'''
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列， # 同时列出数据和数据下标，一般用在 for 循环当中。

from cal_time import *

# 线性查找
@cal_time
def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
        else:
            return None


# 二分查找
@cal_time
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right: # 候选区有值就要一直查找
        mid = (left + right) // 2  # 整除2
        if li[mid] == val:
            return mid
        elif li[mid] > val: # 要找的值在mid左侧
            right = mid - 1 # 中间往左移动
        else: # 要找的值在mid右侧
            left = mid + 1 # 中间往右移动
    else: # 找不到
        return None

# li = [1, 3, 4, 5, 6, 7, 8, 9]
# print(binary_search(li, 3))

# li = list(range(10000))
# linear_search(li, 3890)
# binary_search(li, 3890)



















