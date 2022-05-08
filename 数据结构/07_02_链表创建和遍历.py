'''
头插法：


尾插法：




'''

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


def create_linklist_head(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head

def print_linklist(lk):
    while lk:
        print(lk.item, end=',')
        lk = lk.next


lk = create_linklist_head([1, 2, 3])
print(lk.item)
print(print_linklist(lk))



def create_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head
