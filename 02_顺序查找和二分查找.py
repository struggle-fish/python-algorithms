'''
    查找：在一些数据元素中，通过一定的方法找出与给定关键字相同的数据元素的过程

    列表查找（线性查找）：从列表中查找指定元素
        输入：列表，待查找元素
        输出：元素下标(找不到返回None 或者 -1)
    内置列表查找函数：index()


    顺序查找：也叫线性查找，从列表的第一个元素开始，顺序进行搜索，直到找到元素或搜索到列表最后一个元素为止。

    二分查找：从有序列表的初始候选区li[0:n]开始，通过对待查找的值与候选区中间值的比较，可以使候选区减少一半。
'''


# 线性查找
def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
        else:
            return None


# 二分查找
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right: # 候选区有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val: # 要找的值在mid左侧
            right = mid - 1
        else: # 要找的值在mid右侧
            left = mid + 1
    else: # 找不到
        return None























