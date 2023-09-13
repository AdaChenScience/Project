w=float(input('请输入w:'))
x=float(input('请输入x:'))
y=float(input('请输入y:'))
z=float(input('请输入z:'))
l=[w,x,y,z]
l.sort(reverse=True)
print('这三个数从大到小依次为:',*l)