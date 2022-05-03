'''
假设现在的列表分两段有序，如果将其合成为一个有序列表
2 5 7 8 9 | 1 3 4 6

这种操作称为一次归并


使用归并：
    分解：将列表越分越小，直至分成一个元素
    终止条件：一个元素是有序的
    合并：将两个有序类表归并，列表越来越大
'''

def merge(li, low, mid, high):
    '''
    :param li:
    :param low: 开始
    :param mid: 中间
    :param high: 结尾
    :return:
    '''
    i = low  # 左边开始
    j = mid + 1 # 右边开始
    ltmp = []
    while i <= mid and j <=high: # 只要左右两边都有数
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    # while 执行完，肯定有一部分没数
    while i <= mid: # 第一部分有数，第二部分没数了
        ltmp.append(li[i])
        i += 1
    while j <= high: # 第二部分有数，第一部分没数了
        ltmp.append(li[j])
        j += 1
    li[low:high + 1] = ltmp # 回写数据


li = [2, 4, 5, 7, 1, 3, 6, 8] # 左边部分 2 4 5 7  右边部分 1 3 6 8 左右两边都是有序的，执行一次归并
merge(li, 0, 3, 7)
print(li)

def merge_sort(li, low, high):
    '''
    :param li:
    :param low:  最小
    :param high: 最大
    :return:
    '''
    if low < high: # 至少有两个元素，递归
        mid = (low + high) // 2
        merge_sort(li, low, mid) # 左边
        merge_sort(li, mid + 1, high) # 右边
        merge(li, low, mid, high) # 合并



li2 = list(range(1000))
import random
random.shuffle(li2)
print('原始',li2)
merge_sort(li2, 0, len(li2) - 1)
print('排好', li2)



# def merge_sort_test(li, low, high):
#     if low < high: # 至少有两个元素，递归
#         mid = (low + high) // 2
#         merge_sort_test(li, low, mid) # 左边
#         merge_sort_test(li, mid + 1, high) # 右边
#         print('排', li[low:high+1])
#
#
# li2 = list(range(10))
# import random
# random.shuffle(li2)
# print('原始',li2)
# merge_sort_test(li2, 0, len(li2) - 1)
# print('排好', li2)


















