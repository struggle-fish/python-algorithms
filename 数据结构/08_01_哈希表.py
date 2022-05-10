'''
哈希表：
    一个通过哈希函数来计算数据存储位置的数据结构，通常支持如下操作：
        inster(key, value): 插入键值对
        get(key): 如果存在键为key的键值，则返回value, 否则返回空值
        delete(key): 删除键为key的键值对


哈希：
    key 为k 的元素放到k位置上
    改进直接寻址表：哈希
        构建大小为m的寻址表T
        key 为k 的元素放到 h(k) 位置上
        h(k) 是一个函数，其将域U 映射到表T[0, 1, 2, 3, ... , m-1]


哈希表（Hash Table, 又称为散列表），是一种线性表的存储结构，哈希表由一个直接寻址表和一个哈希函数组成。哈希函数h(k)将元素关键字k 作为自变量，返回
元素的存储下标。

假设有一个长度为7的哈希表，哈希函数h(k)= k % 7 。元素集合{14, 22, 3, 5}存储如下：

i:0     14
i:1     22
i:2
i:3     3
i:4
i:5     5
i:6


哈希冲突：
    由于哈希表的大小是有限的。而要存储的值的总数量是无限的。因此对于任何哈希函数，都会出现两个不同元素映射到同一个位置上的情况，这种情况
    叫哈希冲突

    比如：h(k) = k % 7, h(0) = h(7) = h(14)


解决哈希冲突-开放寻址法（费劲）

开放寻址法：如果哈希函数返回的位置已经有值，则可以向后探查新的位置来存储这个值。
线性探查：如果位置i被占用，则探查i+1, i+2 ...
二次探查：如果位置i被占用，则探查i+1(平方2) ...
二度哈希：有n个哈希函数，当使用第1个哈希函数h1发生冲突时，则尝试使用h2, h3...


解决哈希冲突-拉链法

拉链法：哈希表每个位置都连接一个链表，当冲突时，冲突的元素将被加到该位置链表的最后


哈希函数：
    除法哈希函数：h(k) = k % m
    乘法哈希函数：h(k) = floor(m*(A*key%1))
    全域哈希法：表达式不好写处理，查查吧

'''

class LinkList:
    # 节点创建
    class Node:
        def __init__(self, item=None):
            self.item = item
            self.next = None

    # 迭代器
    class LinkListIterator:
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):
        return '<<' + ','.join(map(str, self)) + '>>'



# lk = LinkList([1,2,3,4,5])
# print(lk)
# for element in lk:
#     print(element)


# 哈希表
class HashTable:
    def __init__(self, size = 101):
        self.size = size
        self.T = [LinkList() for i in range(self.size)]

    def h(self, k):
        return k % self.size

    def insert(self, k):
        i = self.h(k)
        if self.find(k):
            print('重复的插入')
        else:
            self.T[i].append(k)

    def find(self, k):
        i = self.h(k)
        return self.T[i].find(k)


ht = HashTable()
ht.insert(0)
ht.insert(1)
# ht.insert(0)
ht.insert(3)
ht.insert(102)
ht.insert(90)
ht.insert(508)
print(','.join(map(str, ht.T)))

print(ht.find(508))




























