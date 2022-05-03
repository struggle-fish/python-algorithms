'''
计数排序：
    对列表进行排序，已知列表中的数范围都在0到100之间，设计时间复杂度为O(n)的算法

'''

'''
1 3 2 4 1 2 3 1 3 5

0 0
1 3
2 2
3 3
4 1
5 1

1 1 1 2 2 3 3 3 4 5

'''

def count_sort(li, max_count = 10):
    count = [0 for _ in range(max_count + 1)]
    for val in li:
        count[val] += 1
    print(count)
    li.clear()
    for ind, val in enumerate(count): # 下标就是数，值是有几个
        for i in range(val):
            li.append(ind)



import random
li = [random.randint(0, 10) for _ in range(10)]
print(li)
count_sort(li)
print(li)

'''

[7, 10, 0, 6, 3, 9, 9, 0, 3, 3]
0   1  2  3  4  5  6  7  8  9  10
[2, 0, 0, 3, 0, 0, 1, 1, 0, 2, 1]
[0, 0, 3, 3, 3, 6, 7, 9, 9, 10]

'''