'''
队列是一个数据集合，仅允许在列表的一端进行插入，另一端进行删除

进行插入的一端称为队尾，插入动作称为进队，或入队

进行删除的一端称为队头，删除动作称为出队

队列的性质：先进先出（First-in, First-out）


环形队列
    当队尾指针front == MaxSize - 1时，在前进一个位置就自动到 0

    队首指针前进1： front = (front + 1) % MaxSize
    队尾指针前进1：rear = (rear + 1) % MaxSize
    队空条件：rear == front
    队满条件：（rear + 1）% MaxSize == front
'''

class Queue:
    def __init__(self, size = 100):
        self.queue = [0 for _ in range(size)]
        self.rear = 0 # 队尾指针
        self.front = 0 # 队首指针
        self.size = size

    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise RuntimeError('队满了~')

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError('队列空~')
    def is_empty(self):
        return self.rear == self.front

    def is_filled(self):
        return (self.rear + 1) % self.size == self.front




q = Queue(5)

for i in range(4):
    q.push(i)

print(q.is_filled())
print(q.pop())
q.push(9)









