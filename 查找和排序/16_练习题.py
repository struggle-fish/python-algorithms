'''
题目1：
    给两个字符串 s 和 t，判断t 是否为 s 的重新排列后组成的单词

    s = 'anagram' , t = 'nagaram'  return true

    s = 'rat', t = 'car'  return false


题目2：
    给定一个m*n的二维列表，查找一个数是否存在，列表有下列特性：
    每一行的列表从左到右已经排序好
    每一行的第一个数比上一行最后一个数大

    [
        [1, 3, 5, 7],
        [10, 11, 16, 20]
        [23, 30, 34, 50]
    ]

题目3：
    给定一个列表和一个整数，设计算法找到两个数的下标，使得两个数之和为给定的整数，保证肯定仅有一个结果

    例如：列表[1, 2, 5, 4] 与目标整数3 ， 1+2 = 3 结果为（0,1）
'''


# 题目一
def isAnagram(self, s, t):
    ss = list(s)
    tt = list(t)

    ss.sort()
    tt.sort()
    return ss == tt



def isAnagram2(s, t):
    return sorted(list(s)) == sorted(list(t))


def isAnagram3(s, t):
    dict1 = {} # { 'a': 1, 'b': 2 }
    dict2 = {}

    for ch in s:
        dict1[ch] = dict1.get(ch, 0) + 1 # 存在就+1 不存在就0
    for ch in t:
        dict2[ch] = dict2.get(ch, 0) + 1

    return dict1 == dict2



# 题目二
def searchMatrix(matrix, target):
    for line in matrix:
        if target in line:
            return True
    return False

def searchMatrix2(matrix, target):

    h = len(matrix)
    if h == 0:
        return False # []
    w = len(matrix[0])
    # [[], [], []]
    if w == 0:
        return False
    left = 0
    right = w * h -1
    # 找对应数的位置 行和列
    '''
    0  1  2   3
    4  5  6   7
    8  9  10  11
    行i = num // 4
    列j = num % 4
    '''
    while left <= right:
        mid = (left + right) // 2
        i = mid // w
        j = mid % w
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            right = mid
        else:
            left = mid + 1
    else:
        return False


li = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
#
# print(searchMatrix2(li, 300))


# 题目三
def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i):
            if nums[i] + nums[j] == target:
                return sorted([i, j])


# 没有排好序的





# 如果是有序的
# {2, 7, 11, 15} target = 9
def binary_search(li, left, right, val):
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None

def twoSum2(nums, target):
    n = len(nums)
    for i in range(n):
        a = nums[i]
        b = target - a
        if b >= a:
            j = binary_search(nums, i+1, len(nums) - 1, b)
        else:
            j = binary_search(nums, 0, i - 1, b)
        if j:
            break
    return sorted([i+1, j+1])


nums = [2, 7, 11, 15]
print(twoSum2(nums, 9))








