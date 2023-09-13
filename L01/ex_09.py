l1=[float(i) for i in list(input('请输入L(元素以空格隔开):').split(' '))]
l2=l1[:]
# for-loop
for i in range(len(l1)//2):
    l1[i],l1[-1-i]=l1[-1-i],l1[i]
print(l1)
# while-loop
i=0
while i<len(l2)//2:
    l2[i],l2[-1-i]=l2[-1-i],l2[i]
    i+=1
print(l2)