'''
每次都去循环一遍，找最小的，拿出来，在重复一遍
两个交换

关键点：有序区、无序区、无序区最小数的位置
'''

# 不推荐，多占用一份内存，数据量大的话资源很大
def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new

# li = [3, 2, 4, 1, 4, 9, 18, 3, 11]
# print(select_sort_simple(li))


def select_sort(li):
    for i in range(len(li) - 1): # 第几趟
        min_loc = i # 假定无序区第一个就是最小的值， 无序区第一个值就是 i
        print(min_loc)
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        # 找到了最小值，和无序区的第一个值交换
        if min_loc != i:
            li[i], li[min_loc] = li[min_loc], li[i]
        print(f'第{i}', li)
li = [5, 2, 4, 1, 6, 9, 18, 3, 11]
print('原始', li)
print(select_sort(li))



















