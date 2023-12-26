'''
你也能看得懂的 python 算法书


'''

arr1 = [1, 3, 4, 6, 10]
arr2 = [2, 5, 8, 11]

ind = 0
ans = arr1.copy()  # ans 初始化为 arr1

for i in range(0, len(arr2)):
    while ind < len(arr1):
        if arr2[i] <= arr1[ind]:  # ind 的范围不能超过数组下标的最大值
            ans.insert(ind + i, arr2[i])  # 向第一个数组中合适位置插入第二个数组中的元素
            break
        else:
            ind += 1  # 如果arr2[i]大于arr1[ind]，则将ind向后移动一位，继续比较下一个元素。
    else:
        # 如果内层循环正常结束（即ind已经达到arr1的末尾），则说明arr1已经遍历完，剩下的arr2[i:]
        # 中的元素都比arr1中的元素大。此时，将剩余的arr2[i:]
        # 直接拼接到ans数组的末尾，并使用break语句跳出外层循环。
        ans = ans + arr2[i:]  # 如果 arr1 已经遍历完了，直接把剩下的arr2 拼接到 arr1 后面
        break
print(ans)
