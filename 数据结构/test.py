def func2(x):
    print('输入值', x)
    if x > 0:
        func2(x - 1)
        print('当前值', x)
    print('执行后的', x)
func2(5)