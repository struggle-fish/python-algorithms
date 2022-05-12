'''
二叉树的链式存储：将二叉树的节点定义为一个对象，节点之间通过类似链表的链接方式来连接

节点定义：
    class BitreeNode:
        def __init__(self, data):
            self.data = data
            self.lchild = None
            self.rchild = None

'''


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
print(root.lchild.rchild.data)






