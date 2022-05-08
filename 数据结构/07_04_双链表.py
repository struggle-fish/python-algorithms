'''
双链表的每个节点有两个指针：一个指向后一个节点，另一个指向前一个节点

双链表的插入
    p.next = curNode.next
    curNode.next.prior = p

    p.prior = curNode
    curNode.next = p


双链表的删除：
    p = curNode.next
    curNodex.next = p.next
    p.next.prior = curNode
    del p
'''

