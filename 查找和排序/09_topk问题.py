'''
现在有 n 个数，设计算法得到前K大的数， （k < n）

解决思路：
    排序后切片 O(nlogn)
    排序LowB三人组  O(mn)
    堆排序思路 O(nlogk)

    取列表前K个元素建立一个小根堆。堆顶就是目前第K大的数。
    依次向后遍历原列表，对于列表中的元素，如果小于堆顶，则忽略该元素；如果大于堆顶，则将堆顶更换为该元素。并且对堆进行一次调整。
    遍历列表所有元素后，倒序弹出堆顶
'''

'''
[ 6, 8, 1, 9, 3, 0, 7, 2, 4, 5 ]  => 5, 6, 7, 8, 9

'''


def sift(li, low, high):
    """
    :param li: 列表
    :param low: 堆的根节点位置  每次都是当前最大一个
    :param high: 堆的最后一个元素的位置
    :return:
    """
    i = low
    j = 2 * i + 1
    temp = li[low]
    while j <= high:
        if j + 1 <= high and li[j+1] < li[j]:  # 小根堆
            j = j + 1
        if li[j] < temp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = temp
            break
    else:
        li[i] = temp


def topk(li, k):
    heap = li[0:k] # 先取出前 k 个数
    for i in range((k-2)//2, -1, -1):
        sift(heap, i, k - 1)
    # 建堆-结束
    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k - 1)
    print(heap, '哈哈')
    # 遍历-结束
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    # 出数-结束
    return heap

li = [ 6, 8, 1, 9, 3, 0, 7, 2, 4, 5 ]
# import random
# li = list(range(1000))
# random.shuffle(li)
print(topk(li, 5))





































