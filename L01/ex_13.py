def f(x):
    if x==1:
        return 1
    return x*f(x-1)
n=int(input('请输入n:'))
print('%d的阶乘为%d'%(n,f(n)))