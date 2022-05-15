'''
有 n 个非负整数，将其按照字符串拼接的方式拼接为一个整数。
如何拼接可以使得得到的整数最大？

例如：32， 94， 128， 1286， 6， 71 可以拼接的最大整数为

94 71 6 32 1286 128


'''
from functools import cmp_to_key

li = [32,94,128,1286,6,71]
def xy_cmp(x, y):
    if x + y < y + x:
        return 1  # x 大于 y
    elif x + y > y + x:
        return -1
    else:
        return 0

def number_join(li):
    li = list(map(str, li))
    li.sort(key=cmp_to_key(xy_cmp))
    return ''.join(li)

print(number_join(li))





