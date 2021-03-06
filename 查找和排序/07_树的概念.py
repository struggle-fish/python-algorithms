'''
堆排序前传-树与二叉树

树是一种数据结构, 比如： 目录结构
树是一种可以递归定义的数据结构

树是由n个节点组成的集合：
    如果 n = 0 , 那就是一颗空树
    如果 n > 0 , 那存在1个节点作为树的根节点，其他节点可以分为 m 个集合，每个集合本身又是一棵树


树的基本概念：
根节点，叶子节点
树的深度（高度）
树的度（分了几个岔）
孩子节点/父节点
子树
'''

'''
二叉树
度不超过2的树

每个节点最多有两个孩子节点

两个孩子节点被区分为做孩子节点和右孩子节点

'''

'''
满二叉树：一个二叉树，如果每一个层的节点数都达到最大值，则这个二叉树就是满二叉树

完全二叉树：叶节点只能出现在最下层和次下层，并且最下面一层的节点都集中在该层最左边的若干位置的二叉树
只能在最后一层少节点，其他层得是满的，最后一层也得是连续的，不能跳着少，最下层可以不满，但是必须得从左往右不间断排着
'''


'''
二叉树的存储方式
链式存储方式
顺序存储方式 -> 用列表存

'''

'''
顺序存储：

[9, 8, 7, 6, 5, 0, 1, 2, 4, 3]
 0  1  2  3  4  5  6  7  8  9

                                9（0）
                            /          \
                        8（1）          7（2）
                       /      \       /       \
                    6（3）     5（4） 0（5）     1（6）
                  /     \    /    \ 
              2（7）   4（8）3（9）
   
父节点和左孩子节点编号下标关系：
0 - 1 1-3 2-5 3-7 4-9
父    子
i -> 2i+1

父节点和右孩子节点编号下标关系：
0-2  1-4  2-6  3-8 4-10

父    子
i -> 2i+2


父亲找孩子，，孩子找父亲

'''















































