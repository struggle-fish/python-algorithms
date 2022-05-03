'''
多关键字排序：假如现在有一个员工表，要求按照薪资排序，年龄相同的员工按照年龄排序。


先按照年龄进行排序，在按照薪资进行稳定的排序

对 32 13 94 52 17 54 93 排序，是否可以看做多关键字排序？

桶是有序的

'''



def radix_sort(li):
    max_num = max(li) # 找最大值 99 -> 2 888-> 3  10000->5
    it = 0 # 迭代次数
    while 10 ** it <= max_num: # 第几次分桶
        buckets = [[] for _ in range(10)]
        for val in li:
            # 987  it = 1 取 8出来  987 // 10 => 98  98 % 10 => 8
            #      it = 2 取 9出来  987 // 100 => 9  9 % 10 => 9
            digit = (val // 10 ** it) % 10
            buckets[digit].append(val)
        # 分桶结束
        li.clear()
        for buc in buckets:
            li.extend(buc)
        # 重写入li

        it += 1


li = list(range(100))
import random
random.shuffle(li)
radix_sort(li)
print(li)























