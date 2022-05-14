'''
AVL树：是一棵自平衡的二叉树
AVL树具有以下性质：
    根的左右子树的高度之差的绝对值不能超过1
    根的左右子树都是平衡二叉树



AVL 树 - 插入
插入一个节点可能会破坏AVL树的平衡，可以通过旋转操作来进行修正
插入给一个节点后，只有从插入节点到根节点的路径上的节点的平衡可能被改变，
我们需要找出第一个破坏了平衡条件的节点，称之为K，K的两颗子树的高度差2

不平衡的出现可能有4种情况
1、左旋- 不平衡是由于对K的右孩子的右子树插入导致的  -> 右右 - 左旋
2、右旋- 不平衡是由于对K的左孩子的左子树插入导致的  -> 左左 - 右旋
3、右旋-左旋 - 不平衡是由于对K的右孩子的左子树插入导致的 -> 右左 -> 右旋-左旋
4、左旋-右旋 - 不平衡是由于对K的左孩子的右子树插入导致的 -> 左右 -> 左旋-右旋


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






class AVLNode(BiTreeNode):
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0



# 用右边 减去 左边 = bf值  左边沉了 -1 右边沉了 1
# 左边插入后，左边沉了 bf = -1


class AVLTree(BST):
    def __init__(self, li=None):
        BST.__init__(self, li)

    # 左旋 一定要对照着旋转前和旋转后的图看
    def rotate_left(self, p, c):
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        c.lchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    # 向右旋转
    def rotate_right(self, p, c):
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p

        c.rchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    # 右旋-左旋
    def roate_right_left(self, p, c):
        g = c.lchild

        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c

        g.rchild = c
        c.parent = g

        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g

        # 更新 bf
        if g.bf > 0:
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else: # 插入的是g
            p.bf = 0
            c.bf = 0
        return g

    # 左旋-右旋
    def roate_left_right(self, p, c):
        g = c.rchild

        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c

        g.lchild = c
        c.parent = g

        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g

        # 更新 bf
        if g.bf > 0:
            p.bf = 0
            c.bf = -1
        elif g.bf < 0:
            p.bf = 1
            c.bf = 0
        else: # 插入的是g
            p.bf = 0
            c.bf = 0
        return g




    def insert_no_rec(self, val):
        # 1、和 二叉搜索树一样，插入
        p = self.root
        if not p:  # 空树
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data: # 去左子树
                if p.lchild:
                    p = p.lchild
                else:  # 左子树不存在
                    p.lchild = AVLNode(val)
                    p.lchild.parent = p
                    node = p.lchild # node 存储是插入的节点
                    break
            elif val > p.data: # 去右子树
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = AVLNode(val)
                    p.rchild.parent = p
                    node = p.rchild
                    break
            else: # val == p.data
                return

        # 2、更新 balance factor bf
        while node.parent: # node.parent 不空
            if node.parent.lchild == node: # 传递是从左子树来的，左子树更沉了
                # 更新node.parent 的 bf -= 1
                if node.parent.bf < 0: # 原来 node.parent.bf == -1 ,更新后变成 -2
                    # 看 node那边沉 左边沉->右旋   右边沉 -> 左旋-右旋
                    g = node.parent.parent # 为了连接旋转之后的子树
                    x = node.parent # 旋转前的 子树的根
                    if node.bf > 0:
                        n = self.roate_left_right(node.parent, node)
                    else:
                        n = self.rotate_right(node.parent, node)
                    # 记得 把 n 和 g 连起来
                elif node.parent.bf > 0: # 原来 node.parent.bf = 1 ,更新后减1 变成0
                    node.parent.bf = 0
                    break
                else: # 原来的 node.parent.bf = 0, 更新之后变成 -1
                    node.parent.bf = -1
                    node = node.parent
                    continue
            else: # 传递是从右子树来的，右子树更沉了
                # 更新后的 node.parent.bf += 1
                if node.parent.bf > 0: # 原来node.parent.bf = 1, 更新后变成2
                    # 做旋转
                    # 看 node 那边沉
                    g = node.parent.parent
                    x = node.parent  # 旋转前的 子树的根
                    if node.bf < 0: # node 左边沉 node.bf = 1
                        n = self.roate_right_left(node.parent, node)
                    else: # node.bf = -1
                        n = self.rotate_left(node.parent, node)
                    # 记得 n 和 g 连起来
                elif node.parent.bf < 0: # 原来的node.parent.bf = -1 , 更新之后变成0
                    node.parent.bf = 0
                    break
                else: # 原来的 node.parent.bf = 0, 更新之后 变成1
                    node.parent.bf = 1
                    node = node.parent
                    continue
            # 链接旋转后的 子树
            n.parent = g
            if g: # g 不是空
                if x == g.lchild:
                    g.lchild = n
                else:
                    g.rchild = n
                break
            else:
                self.root = n
                break




tree = AVLTree([9, 8, 7, 6, 5, 4, 3, 2, 1])
tree.pre_order(tree.root)
print('')
tree.in_order(tree.root)










