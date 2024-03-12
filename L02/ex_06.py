c=2
k=int(input('请输入所除系数:'))
g=c/k
i=0
while abs(c-g*g)>0.00000000001:
    g=(g+c/g)/2
    i+=1
    print('%d:g=%.13f'%(i,g))