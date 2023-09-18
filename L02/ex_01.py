product=[1]
sequence=[[1]]
n=int(input('请输入n:'))
for i in range(1,n):
    max_p=0
    index=0
    for j in range(i):
        if product[j]*product[i-1-j]>max_p:
            index=j
            max_p=product[j]*product[i-1-j]
    if i+1>max_p:
        product.append(i+1)
        sequence.append([i+1])
    else:
        product.append(max_p)
        sequence.append(sequence[index]+sequence[i-1-index])
print('最大乘积为:',product[-1])
print('所求正整数列为:',sequence[-1])