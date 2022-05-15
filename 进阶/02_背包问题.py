'''
一个小偷在某个商店发现有N个商品，第i个商品价值 v(i)元，重w(i)千克，他希望拿走的价值尽量高，但他的背包最多只能容纳w千克的东西，
他应该拿走哪些商品

0-1 背包：对于一个商品，小偷要么把他完整拿走，要么留下，不能只拿走一部分，或把一个商品拿走多次（商品为金条）

分数背包：对于一个商品，小偷可以拿走其中任意一部分。（商品为金砂）

'''

'''
举例：
    商品1： v1 = 60 w1= 10
    商品2： v2 = 100 w2 = 20
    商品3： v3 = 120 w3 = 30
    
    背包容量： w = 50
    
    对于0-1背包分数背包，贪心算法是否都能得到最优解？为什么？
    
'''

# 分数背包 先拿单位里最值钱的

goods = [(60, 10), (100, 20), (120, 30)] # 每个商品元祖表示 （价格，重量）
goods .sort(key = lambda x: x[0] / x[1], reverse=True) # 先排序
# print(goods)
def fractional_backpack(goods, w):
    m = [0 for _ in range(len(goods))]
    total_v = 0
    for i, (price, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            total_v += price
            w -= weight # 包剩下还能装多少
        else:
            m[i] = w / weight
            total_v += m[i] * price
            w = 0  # 背包只能拿一个
            break
    return m, total_v

print(fractional_backpack(goods, 50))














