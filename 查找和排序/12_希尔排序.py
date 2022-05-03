'''
希尔排序：是一种分租插入排序算法

首先取一个整数 d1 = n / 2, 将元素分为 d1 个组，每组相邻两元素之间距离为d1，在各组内进行直接插入排序

取第二个整数d2 = d1 / 2，重复上述分组排序过程，知道d1 = 1，即所有元素在同一组内进行直接插入排序

希尔排序每趟并不使某些元素有序，而是使整体数据越来越接近有序；最后一趟排序使得所有数据有序。

'''

'''
5 7 4 6 3 1 2 9 8   d = 4  => d = 2 => d = 1

5       3       8
  7        1
   4        2
     6       9
'''



def insort_sort_gat(li, gap):
    for i in range(gap, len(li)): # i 表示摸到的牌的下标
        tmp = li[i]
        j = i - gap # j 指的是手里的牌的下标
        while j >= 0 and li[j] > tmp:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp



def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insort_sort_gat(li, d)
        d //= 2



li = list(range(1000))
import  random
random.shuffle(li)
shell_sort(li)
print(li)





