'''
    递归的特点
    1、调用自身
    2、结束条件

    def fun1(x):
        if x > 0:
            print(x)
            fun1(x - 1)
'''

# 汉诺塔  A B C 三个柱子

'''
    n = 2 时：
    1、把小圆盘从 A 移动到 B
    2、把大圆盘从 A 移动到 C
    3、把小圆盘从 B 移动到 C
    
    当为 n 的时候
    上面 n - 1个 看成一个整体，剩下最后一个 ，这样就是两部分了
    1、把 n -1 个盘子从A经过C移动到B
    2、把第n个盘子从A移动到C
    3、把n - 1个盘子从B经过A移动到C
    
'''

def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b) # 第一步 n - 1 个盘子从 a 经过 c 移动到 b
        print('移动 %s to %s' % (a, c))
        hanoi(n-1, b, a, c)


hanoi(3, 'A', 'B', 'C')
















