'''
桶排序：
    在计数排序中，如果元素的范围比较大（比如在1到1亿之间）
    如果改造算法？


    桶排序，首先将元素分在不同的桶中，在对每个桶中的元素排序

'''

def bucket_sort(li, n = 100, max_num = 10000):
    '''
    :param li:
    :param n: 桶
    :param max_num: 最大值
    :return:
    '''
    buckets = [[] for _ in range(n)] # 创建桶
    for val in li:
        i = min(val // (max_num // n), n - 1) # i 表示 val 放到几号桶里
        buckets[i].append(val) # 把val 放到桶里
        for j in range(len(buckets[i]) - 1, 0, -1): # 对每个桶里排序
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break

    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)
    return sorted_li


import random
li = [random.randint(0, 10000) for i in range(1000)]
# print(li)
li = bucket_sort(li)
print(li)

















