'''
链表是由一系列节点组成的元素集合。每个节点包含两部分，数据域item和指向下一个节点的指针next

通过节点之间的相互连接，最终串联成一个链表



'''

# 单向链表

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


# 手动创建一个链表
a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

print(a.next.next.item) # 3