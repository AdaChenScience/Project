def cal(n):
    if n==1:
        return 1
    if n<1:
        l=n
        r=1
    else:
        l=1
        r=n
    while r-l>0.0000001:
        mid=(l+r)/2
        if mid*mid*mid==n:
            return mid
        elif mid*mid*mid<n:
            l=mid
        else:
            r=mid
    return (l+r)/2

y=float(input('请输入y:'))
flag=0 if y>0 else 1
print('%f的立方根约为%f'%(y,(-1)**flag*cal(abs(y))))