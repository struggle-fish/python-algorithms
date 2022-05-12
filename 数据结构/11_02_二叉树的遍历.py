'''
二叉树的遍历方式：
    前序遍历 EACBDGF
    中序遍历 ABCDEGF
    后序遍历 BDCAFGE
    层次遍历 EAGCFBD

            E
        /       \
      A         G
      \         \
        C         F
    /      \
  B         D
'''
from collections import deque

class BitreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None # 左孩子
        self.rchild = None # 右孩子


a = BitreeNode('A')
b = BitreeNode('B')
c = BitreeNode('C')
d = BitreeNode('D')
e = BitreeNode('E')
f = BitreeNode('F')
g = BitreeNode('G')

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e

# 前序遍历
def pre_order(root):
    if root:
        print(root.data, end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)

# pre_order(root)

def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end=',')
        in_order(root.rchild)

# in_order(root)

def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=',')


# post_order(root)



def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft() # 出队
        print(node.data, end=',')
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)


level_order(root)
