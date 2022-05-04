'''
栈是一个数据集合，可以理解为只能在一端进行插入或删除操作的列表

栈的特点：后进先出 LIFO（last-in, first-out）

栈的概念：栈顶，栈底

栈的基本操作：
    进栈（压栈）：push
    出栈：pop
    取栈顶：gettop

使用一般的列表结构即可实现栈
    进栈：li.append
    出栈：li.pop
    取栈顶：li[-1]
'''

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, element):
        self.stack.append(element)
    def pop(self):
        return self.stack.pop()
    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
    def is_empty(self):
        return len(self.stack) == 0



# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.pop())




'''
栈的应用-括号匹配问题
给一个字符串，其中包含小括号，中括号，大括号，求该字符串中的括号是否匹配

例如：
()()[]{}  匹配
([{()}])  匹配
[](       不匹配
[(])      不匹配

思路：
    进栈出栈 -> 栈是空的，就OK
'''


def brace_match(s):
    stack = Stack()
    math = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    for ch in s:
        if ch in { '(', '[', '{' }:
            # 进栈
            stack.push(ch)
        else: # ch in { ')', ']', '}' }
            if stack.is_empty():
                return False
            elif stack.get_top() == math[ch]:
                stack.pop()
            else: # 栈顶不匹配
                return False
    if stack.is_empty():
        return True
    else:
        return False









































