'''
排序： 将一组无序的记录序列调整为 有序的记录序列

列表排序：将无序的变为有序的列表
    输入：列表
    输出：有序的列表

升序和降序
内置函数：sort()


常见的排序算法：
    排序 Low B三人组：冒泡排序、选择排序、插入排序
    排序NB 三人组：快速排序、堆排序、归并排序
    其他排序：希尔排序、计数排序、基数排序

动图：https://www.runoob.com/w3cnote/ten-sorting-algorithm.html
'''

# 冒泡排序
import random

'''
列表每两个相邻的数，如果前面比后面打，则交换这两个数。
一趟排序完后，则无序区减少一个数，有序区增加一个数。

整个过程执行n-1趟
当剩下一个的时候，是不需要在执行了，所以指针比趟少1次运行
'''

def bubble_sort(li):
    for i in range(len(li) - 1): # 第 i 趟
        exchange = False
        for j in range(len(li) - i - 1): # 指针
            # 如果在一趟过程中，没有发生交换，就认为已经排好序了，可以不用继续进行交换了
            if li[j] > li[j+1]: # 交换 改成小于号就是 降序了
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        print(f'第{i}', li)
        if not exchange: # not是逻辑判断词，用于布尔型True和False，not True为False，not False为True
            return

# li = [2, 4, 1, 6,20, 3, 5, 0,]
li = [9, 8, 7, 1, 2, 3, 4, 5, 6]
print('原始', li)
bubble_sort(li)

# li = [random.randint(0, 1000) for i in range(1000)]
# print(li)
# print('结束----------------------------')
# bubble_sort(li)
# print(li)










