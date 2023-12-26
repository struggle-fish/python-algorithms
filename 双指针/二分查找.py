'''
你也能看得懂的 python 算法书

第二个问题也是有关有序数组的问题。
如何快速在一个有序数组中准确地找到一个元素的位置呢

二分查找又叫 折半查找
意思为每次查找后，查找的范围都折半。
这样查找到最后，查找范围内只剩一个数时，判断它是否为要查找的数。
如果是，就记录它的位置；如果不是，则要查找的数不在这个数组中。


二分查找需要两个指针，
一个指向数组的第一个元素，叫作头指针；
另一个指向数组最后一个元素的后方，叫作尾指针
'''

# [1,3,5,6,7,8,13,14,15,17,18,24,30,43,56]
# 注意，必须是 排序好的
numbers = [1, 3, 5, 6, 7, 8, 13, 14, 15, 17, 18, 24, 30, 43, 56]
head, tail = 0, len(numbers)  # 数组长度刚好是最大下标值 + 1

search = int(input('输入要查找的值'))

while tail - head > 1:  # 当尾指针tail减头指针head等于1时，查找范围内只head有指向的数
    mid = (head + tail) // 2  # mid存储中间数的下标，//2代表对/2的结果舍去分数部分取整
    if search < numbers[mid]:  # search是我们要搜索的元素，如果它小于mid指向的元素
        tail = mid - 1
    if search > numbers[mid]:  # 如果search小于mid指向的元素
        head = mid + 1  # mid指向的元素小于search，所以不用把它保留在范围内
    if search == numbers[mid]:
        ans = mid
        break  # 找到元素的话就直接结束
else:
    if search == numbers[head]:
        ans = head
    else:
        ans = -1  # 如果数组中没有这个元素，那么输出-1

print(ans)
