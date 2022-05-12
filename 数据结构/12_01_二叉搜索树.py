'''
二叉搜索树：
二叉搜索树是一棵二叉树，且满足性质：
设 x 是二叉树的一个节点，
如果 y 是 x 左子树的一个节点，那么 y.key <= x.key,
如果 y 是 x 右子树的一个节点，那么 y.key >= x.key

二叉搜索树的操作：查询，插入，删除

'''

class BiTressNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None



class BST:
    def __init__(self, li = None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)
                # self.insert(val) # TODO 递归方式怎么调用

    # 递归方式 插入
    def insert(self, node, val):
        if not node:
            node = BiTressNode(val)

        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        return node

    # 非递归方式 插入
    def insert_no_rec(self, val):
        p = self.root
        if not p: # 空树
            self.root = BiTressNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else: # 左子树不存在
                    p.lchild = BiTressNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTressNode(val)
                    p.rchild.parent = p
                    return
            else:
                return
    # 先序
    def pre_order(self, root):
        if root:
            print(root.data, end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    # 中序
    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=',')
            self.in_order(root.rchild)

    # 后序
    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=',')

    # 递归 查找
    def query(self, node, val):
        if not node:
            return None
        if node.data < val:
            return self.query(node.rchild, val)
        elif node.data > val:
            return self.query(node.lchild, val)
        else:
            return node
    # 非递归
    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None



tree = BST([4, 6, 7, 9, 2, 1, 3, 5, 8])
# tree.pre_order(tree.root)
# print('')
# tree.in_order(tree.root) # 排好序的
# print('')
# tree.post_order(tree.root)
print(tree.query_no_rec(7).data)


