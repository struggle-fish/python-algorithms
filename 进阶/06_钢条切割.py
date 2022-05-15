'''
某公司出售钢条，出售价格与钢条长度之间的关系如下表：

长度i:   1  2  3  4  5   6   7   8   9   10
价格pi:  1  5  8  9  10  17  17  20  24  30

问题：
现有一段长度为n的钢条和上面的价格表，求切割钢条方案，使得总收益最大

最优子结构：
    可以将求解规模为 n 的原问题，划分为规模更小的子问题：
    完成一次切割后，可以将产生的两段钢条看成两个独立的钢条切割问题

    组合两个问题的最优解，并在所有可能的两段切割方案中选取组合收益最大的，构成原问题的最优解

钢条切割满足最优子结构，问题的最优解由相关子问题的最优解组合而成，这些子问题可以独立求解

'''

'''
动态规划的思想：
    每个子问题只求解一次，保存求解结果
    之后需要此问题时，只需要查找保存的结果
'''

'''
什么问题可以使用动态规划方法？
    最优子结构
    原问题的最优解中涉及多少个子问题
    在确定最优解使用哪些子问题时，需要考虑多少中选择
    
    重叠子问题
    

'''



#    0  1  2  3  4  5   6   7   8   9  10
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def cut_rod_recurrision(p, n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res = max(res, cut_rod_recurrision(p, i) + cut_rod_recurrision(p, n - i))
        return res

# print(cut_rod_recurrision(p, 9))

def cut_rod_recurision(p, n):
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1, n + 1):
            res = max(res, p[i] + cut_rod_recurision(p, n - i))
        return res

# print(cut_rod_recurision(p, 9))


# 动态规划实现， 自底向上
def cut_rod_dp(p, n):
    r = [0]
    for i in range(1, n + 1):
        res = 0
        for j in range(1, i + 1):
            res = max(res, p[j] + r[i-j])
        r.append(res)
    return r[n]
# print(cut_rod_dp(p, 9))


# 输出切割方案
def cut_rod_extend(p, n):
    r = [0]
    s = [0]
    for i in range(1, n + 1):
        res_r = 0 # 价格的最优值
        res_s = 0 # 价格最大值对应方案的左边不切割部分的长度
        for j in range(1, i + 1):
            if p[j] + r[i - j] > res_r:
                res_r = p[j] + r[i-j]
                res_s = j
        r.append(res_r)
        s.append(res_s)
    return r[n], s

def cut_rod_solution(p, n):
    r, s = cut_rod_extend(p, 10)
    ans =[]
    while n > 0:
        ans.append(s[n])
        n -= s[n]
    return ans


# r, s = cut_rod_extend(p, 10)
print(cut_rod_solution(p, 9))



