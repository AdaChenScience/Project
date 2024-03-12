c=2
i=0
g=0
for j in range(0,c+1):
    if j*j>c:
        g=j-1
        break
while c-g*g>0.0001:
    g+=0.00001
    i+=1
    print('%d:g=%.5f'%(i,g))