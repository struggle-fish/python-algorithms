'''
初始时手里（有序区）只有一张牌

每次（从无序区）摸一张牌，插入到手里已有排的正确位置

要摸 n - 1 张牌
'''

def insert_sort(li):
    for i in range(1, len(li)): # i 表示摸到的牌的下标
        tmp = li[i] # 摸到的牌
        j = i - 1 # j 是手里的牌的下标
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j+1] = tmp
        print(li)

li = [3, 2, 4, 1, 5, 7, 9, 6, 8]
print(li)
insert_sort(li)

