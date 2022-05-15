'''
从斐波那契数列看动态规划

斐波那契数列： Fn = F(n-1) + F(n-2)


练习：使用递归，和非递归的方法来求解斐波那契数列的第n项

'''

# 子问题的重复计算
def fibnacci(n):
    if n == 1 or n == 2:
        return 1
    return fibnacci(n-1) + fibnacci(n-2)

# f(5) = f(4) + f(3)
# f(4) = f(3) + f(2)
# f(3) = f(2) + f(1)
# f(3) = f(2) + f(1)
# f(2) = 1
# 相同的问题算了好多遍，所以就很慢
# print(fibnacci(100))


# 动态规划(DP) 的思想，
def fibonacci_no_recurision(n):
    f = [0, 1, 1]
    if n > 2:
        for i in range(n - 2):
            num = f[-1] + f[-2]
            f.append(num)
    return f[n]
print(fibonacci_no_recurision(100))

































