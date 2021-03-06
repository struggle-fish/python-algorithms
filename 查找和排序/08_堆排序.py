'''
堆：一种特殊的完全二叉树结构 （从左到右都是满的）

大根堆：一颗完全二叉树，满足任一节点都比起孩子节点大

小根堆：一颗完全二叉树，满足任一节点都比其孩子节点小


大根堆： 父都比子大
               9
             /   \
           8        7
        /    \    /   \
     6        5  0     1
   /  \     /
  2   4    3


小根堆：父都比子小
                1
             /   \
           2        6
        /    \    /   \
     3        5  7     9
   /  \     /
  4   6    8


堆的性质： 向下调整性
当根节点的左右子树都是堆时，可以通过一次向下的调整来将其变成一个堆。

'''


'''
堆排序的过程：
1、建立堆
2、得到堆顶元素，为最大元素
3、去掉堆顶，将堆最后一个元素放到对顶，此时可通过一次调整重新使堆有序
4、堆顶元素为第二大元素
5、重复步骤3，直到堆变空
'''

# 构建堆  农村包围城市-每次从小的堆开始调整

# 调整函数
def sift(li, low, high):
    """
    :param li: 列表
    :param low: 堆的根节点位置  每次都是当前最大一个
    :param high: 堆的最后一个元素的位置
    :return:
    """
    i = low  # i 最开始指向根节点
    j = 2 * i + 1  # 从父亲找孩子, j 开始是左孩子
    temp = li[low]  # 把堆顶存起来   把省长先扒下来 -> 在查看哪个孩子能当省长 -> 给扒下来的省长找个位置（向下移动）
    # 一直在对比 i 即 low 和 j的大小，如果 j 超过了 high,则说明i就是最后一层了，后面没有了
    while j <= high: # 只要j位置有数
        if j + 1 <= high and li[j+1] > li[j]:    # 如果右有孩子，并且右孩子大，，对比左右孩子谁大
            # 哪个孩子大，就把 j 指向谁
            j = j + 1 # j 指向了右孩子
        if li[j] > temp: # 找到了左右孩子最大的，然后和 当前省长对比，如果孩子大，则出任省长
            li[i] = li[j]
            i = j # 往下看一层  继续往下移动，对比  i 永远指向的是一个空位置
            j = 2 * i + 1
        else: # temp 更大，把 temp放到 i的位置
            li[i] = temp # 把 temp 放到某一级领导位置上
            break
    else:
        li[i] = temp # 把temp 放到叶子节点上



def heap_sort(li):
    n = len(li)
    # 建堆，从最后一个小单元开始，农村包围城市，由下到上
    # 由最后一个叶子节点，找到他的父亲节点  减1除以2，最后一个叶子节点的下标是 n - 1 所以他的父节点就是 (n - 1 -1)/2
    for i in range((n - 2)//2, -1, -1):
        # i 代表了建堆的时候，调整的部分的根的下标
        sift(li, i, n - 1)
    # 建堆完成
    print('建堆', li)
    for i in range(n - 1, -1, -1):
        # i 指向当前堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1) # i - 1 是新的high
    #




li = [i for i in range(100)]
import random
random.shuffle(li)
print('堆原始', li)

heap_sort(li)
print('排序ok', li)






















