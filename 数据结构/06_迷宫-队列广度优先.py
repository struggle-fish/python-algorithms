'''
队列-广度优先搜索 （最短路径）

思路：从一个节点开始，寻找所有接下来的继续走的点，继续不断查找，直到找到出口

使用队列存储当前正在考虑的节点

队列里存的是 当前路的终端 ，找到终点后，倒着找是哪个点出队的

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
'''

from collections import deque


maze = [
   # 0  1  2  3  4  5  6  7  8  9
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 0
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1], # 1
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1], # 2
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1], # 3
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1], # 4
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1], # 5
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1], # 6
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1], # 7
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1], # 8
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 9
]

dirs = [
    lambda x, y: (x + 1, y), # lambda 表示匿名函数
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x, y + 1)
]
def print_r(path):
    curNode = path[-1] # 最后一个元素就是终点
    realPath = []
    while curNode[2] != -1: # (x, y, step) 第二个就是 step
        # realPath.append(curNode[0], curNode[1])
        realPath.append(curNode[0:2])
        curNode = path[curNode[2]] # 找到上一个节点，也就是谁把我带进来的

    realPath.append(curNode[0:2]) # 把起点放进去
    realPath.reverse()
    for node in realPath:
        print(node)

# 这里要注意广度优先搜索首先是会找到所有的可行路径,所以元素入队时候必须要知道当前节点来自哪个节点 也就是nextnode和curnode的联系
def maze_path_queue(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y1, -1)) # 队尾进队
    # 首先注意上下节点的联系需要用单独的列表存储
    path = [] # 存放出队的节点，最后一个节点就是当前出队的节点
    # 队不空
    while len(queue) > 0:
        curNode = queue.popleft()    # 当前节点是队首，队首出队
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            # 终点
            print_r(path)
            return True

        for dir in dirs:
            # 搜索4个方向
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                # 进队
                # 后续节点进队，记录哪个几点带他来的，=> 哪个点出队，导致后续的点进队的
                queue.append((nextNode[0], nextNode[1], len(path) - 1))  # len(path) - 1 => 最后一个元素的下标
                maze[nextNode[0]][nextNode[1]] = 2
    else:
        print('没有路')
        return False


maze_path_queue(1, 1, 8, 8)




