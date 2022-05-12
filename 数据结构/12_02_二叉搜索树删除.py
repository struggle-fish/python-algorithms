'''
1、如果要删除的是叶子节点-直接删除
2、如果要删除的节点只有一个孩子，将此节点的父亲与孩子连接，然后删除该节点
3、如果要删除的节点有两个孩子，将其右子树的最小节点（该节点最多有一个右孩子）删除，并替换当前节点
    找左子树里最大的或者找右子树里最小的

'''




class BiTreeNode:
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
            node = BiTreeNode(val)

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
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else: # 左子树不存在
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
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

    def __remove_node_1(self, node):
        # 情况1 node 是叶子节点
        if not node.parent: # 如果是根的情况
            self.root = None
        if node == node.parent.lchild: # node 是他父亲的左孩子
            node.parent.lchild = None
            node.parent = None
        else:
            # 右孩子
            node.parent.rchild = None

    def __remove_node_21(self, node): # 情况2 node 只有一个孩子 只有左孩子
        if not node.parent: # 根节点
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_22(self, node): # 只有一个右孩子
        if not node.parent:
            self.root = node.rchild
        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, val): # 有两个节点
        if self.root: # 非空树
            node = self.query_no_rec(val)
            if not node:
                return False
            if not node.lchild and not node.rchild: # 叶子节点
                self.__remove_node_1(node)
            elif not node.rchild: # 只有一个左孩子
                self.__remove_node_21(node)
            elif not node.lchild: # 只有一个右孩子
                self.__remove_node_22(node)
            else:
                # 两个孩子都有，先找右边最小的节点, 也就是一直找 lchild
                min_node = node.rchild
                while min_node.lchild:
                    min_node = min_node.lchild
                node.data = min_node.data
                # 删除 min_node
                if min_node.rchild: # 只有右孩子
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)


tree = BST([1, 4, 2, 5, 3, 8, 6, 9, 7])
tree.in_order(tree.root)
print('')
tree.delete(4)
tree.in_order(tree.root)