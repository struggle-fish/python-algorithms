'''
快速排序：快

快速排序思路：
取一个元素P（第一个元素），使元素P归位

列表被P分成两部分，左边都比P小，右边都比P大

递归完成排序

快速排序的问题：
最快情况 左边 右边每次递归的时候都是空，每次都扫1个数
递归

'''

'''
def quick_sort(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid - 1)
        quick_sort(data, mid + 1, right)
'''

# 把数据分成右边大，左边小
def partition(li, left, right):
    tmp = li[left]
    while left < right:
        # 循环找比目标值小的数
        while left < right and li[right] >= tmp: # 从右面找比 tmp 小的数
            right -= 1 # 往左走一步
        li[left] = li[right] # 把右边的值写到左边空位上
        print('右边', li)
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left] # 把左边的值写到右边空位上
        print('左边', li)
    li[left] = tmp # left 和 right碰头了 把tmp 归位
    return left # 返回mid

li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
print('原始', li)
partition(li, 0, len(li) - 1)
print('结果', li)

def quick_sort(li, left, right):
    if left < right: # 至少两个元素
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)

quick_sort(li, 0, len(li) - 1)
print('完成', li)






