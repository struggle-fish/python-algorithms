'''
双向队列：
双向队列的两端都支持进队和出队：


双向队列的基本操作：
    队首进队
    队首出队
    队尾进队
    队尾出队



'''
from collections import deque

# # 创建队列
# q = deque()
# q.append(1) # append 队尾进队
# print(q.popleft()) # popleft 队首出队
#
# # print(q.popleft())
#
# # 用于双向队列
# q.appendleft(1) # 队首进队
# q.pop() # 队尾出队


def tail(n):
    with open('test.text', 'r') as f:
        q = deque(f, n)
        return q

print(tail(5))


